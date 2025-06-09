"""Config flow for De'Longhi DDSX Dehumidifier (based on Ayla IOT) integration."""

import base64
from collections.abc import Mapping
import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN
from homeassistant.helpers import aiohttp_client
from homeassistant.helpers.selector import SelectSelector, SelectSelectorConfig

from .ayla_iot_unofficial import AylaAuthError, new_ayla_api
from .const import (
    API_TIMEOUT,
    COMFORT_APP_ID,
    COMFORT_APP_SECRET,
    CONF_REGION,
    DOMAIN,
    REGION_DEFAULT,
    REGION_EU,
    REGIONS,
)

_LOGGER = logging.getLogger(__name__)

# TODO: Replace this file with one which prompts for username password and country instead of login code

DELONGHI_LOGIN_URL = "https://fidm.eu1.gigya.com/oidc/op/v1.0/3_e5qn7USZK-QtsIso1wCelqUKAK_IVEsYshRIssQ-X-k55haiZXmKWDHDRul2e5Y2/authorize?client_id=1S8q1WJEs-emOB43Z0-66WnL&response_type=code&redirect_uri=https://google.it&scope=openid%20email%20profile%20UID%20comfort%20en&nonce=1743089940407"

DELONGHI_ACCESS_TOKEN_URL = "https://fidm.eu1.gigya.com/oidc/op/v1.0/3_e5qn7USZK-QtsIso1wCelqUKAK_IVEsYshRIssQ-X-k55haiZXmKWDHDRul2e5Y2/token"
DELONGHI_CLIENT_ID = "1S8q1WJEs-emOB43Z0-66WnL"
DELONGHI_CLIENT_PASSWORD = "lmnceiD0B-4KPNN5ZS6WuWU70j9V5BCuSlz2OPsvHkyLryhMkJkPvKsivfTq3RfNYj8GpCELtOBvhaDIzKcBtg"

CONF_LOGIN_TOKEN = "login_token"

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_LOGIN_TOKEN): str,
        vol.Required(CONF_REGION, default=REGION_DEFAULT): SelectSelector(
            SelectSelectorConfig(
                options=[region.lower() for region in REGIONS],
                translation_key=CONF_REGION,
            )
        ),
    }
)
STEP_REAUTH_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_LOGIN_TOKEN): str,
    }
)


class DelonghiConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for De'Longhi DDSX Dehumidifier (based on Ayla IOT)."""

    MINOR_VERSION = 1

    async def _async_validate_credentials(
        self, entry_data: dict[str, Any]
    ) -> dict[str, str]:
        errors: dict[str, str] = {}
        api = new_ayla_api(
            None,
            None,
            COMFORT_APP_ID,
            COMFORT_APP_SECRET,
            europe=entry_data[CONF_REGION] == REGION_EU,
            websession=aiohttp_client.async_get_clientsession(self.hass),
            timeout=API_TIMEOUT,
            token=entry_data[CONF_ACCESS_TOKEN],
        )
        try:
            await api.async_sign_in()
        except TimeoutError:
            errors["base"] = "cannot_connect"
        except AylaAuthError:
            errors["base"] = "invalid_auth"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"

        return errors

    async def _async_fetch_access_token(self, login_token: str) -> str:
        """Fetch access token using the login token."""
        session = aiohttp_client.async_get_clientsession(self.hass)
        auth = f"{DELONGHI_CLIENT_ID}:{DELONGHI_CLIENT_PASSWORD}"
        # TODO: Support non-EU URL as well
        response = await session.post(
            DELONGHI_ACCESS_TOKEN_URL,
            headers={
                "Authorization": f"Basic {base64.b64encode(auth.encode()).decode()}"
            },
            data={
                "grant_type": "authorization_code",
                "code": login_token,
                "redirect_uri": "https://google.it",
            },
        )
        if response.ok:
            body = await response.json()
            access_token = body["access_token"]
            if access_token:
                return access_token, None
        body_text = await response.text()
        return None, "Failed to fetch De'Longhi access token: " + body_text

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input and CONF_LOGIN_TOKEN in user_input:
            try:
                access_token, err = await self._async_fetch_access_token(
                    user_input[CONF_LOGIN_TOKEN]
                )
                if err:
                    errors["base"] = err
                else:
                    entry_data = {
                        CONF_ACCESS_TOKEN: access_token,
                        CONF_REGION: user_input[CONF_REGION],
                    }
                    errors = await self._async_validate_credentials(entry_data)
                    if not errors:
                        return self.async_create_entry(
                            title="De'Longhi access token",
                            data=entry_data,
                        )
            except Exception:
                _LOGGER.exception("Unexpected exception during auth")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            description_placeholders={
                "delonghi_login_url": DELONGHI_LOGIN_URL,
            },
            errors=errors,
        )

    async def async_step_reauth(
        self, entry_data: Mapping[str, Any]
    ) -> ConfigFlowResult:
        """Perform reauth upon an API authentication error."""
        return await self.async_step_reauth_confirm(entry_data)

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Dialog that informs the user that reauth is required."""
        errors: dict[str, str] = {}

        if user_input and CONF_LOGIN_TOKEN in user_input:
            reauth_entry = self._get_reauth_entry()
            try:
                access_token, err = await self._async_fetch_access_token(
                    user_input[CONF_LOGIN_TOKEN]
                )
                if err:
                    errors["base"] = err
                else:
                    data_updates = {CONF_ACCESS_TOKEN: access_token}
                    entry_data = reauth_entry.data | data_updates
                    errors = await self._async_validate_credentials(entry_data)

                    if not errors:
                        return self.async_update_reload_and_abort(
                            reauth_entry, data_updates=data_updates
                        )
            except Exception:
                _LOGGER.exception("Unexpected exception during reauth")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=STEP_REAUTH_DATA_SCHEMA,
            description_placeholders={
                **self.context["title_placeholders"],
                "delonghi_login_url": DELONGHI_LOGIN_URL,
            },
            errors=errors,
        )
