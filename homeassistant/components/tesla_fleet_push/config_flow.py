"""Config Flow for Tesla Fleet integration."""

from __future__ import annotations

from collections.abc import Mapping
import logging
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import aiofiles
import aiohttp
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import jwt
import voluptuous as vol

from homeassistant.components.application_credentials import (
    CONF_AUTH_DOMAIN,
    DOMAIN as APPLICATION_CREDENTIALS_DOMAIN,
    ApplicationCredentialsStorageCollection,
)
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import SOURCE_REAUTH, ConfigFlowResult
from homeassistant.const import CONF_NAME
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    AUDIENCE_DEFAULT,
    CONF_AUDENCE,
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    CONF_DOMAIN,
    CONF_INSTANCE_DOMAIN,
    DOMAIN,
    LOGGER,
)


class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle Tesla Fleet API OAuth2 authentication."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return LOGGER

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow start."""
        errors: dict[str, str] = {}
        placeholders: dict[str, str] = {}
        if user_input:
            err, placeholders = await self.register_tesla_app(user_input)
            if err:
                errors["base"] = err
            return await super().async_step_user()

        private_key_path = Path(
            self.hass.config.path("tesla_fleet_push", "private-key.pem")
        )
        public_key_path = Path(
            self.hass.config.path("tesla_fleet_push", "public-key.pem")
        )
        if not private_key_path.exists() or not public_key_path.exists():
            self.logger.info("Generating new key pair")
            private_key_path.parent.mkdir(parents=True, exist_ok=True)

            private_key = ec.generate_private_key(ec.SECP256R1())
            pem_private_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
            async with aiofiles.open(private_key_path, mode="wb") as f:
                await f.write(pem_private_key)
            self.logger.info("Private key saved to %s", private_key_path)

            public_key = private_key.public_key()
            pem_public_key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            async with aiofiles.open(public_key_path, mode="wb") as f:
                await f.write(pem_public_key)
            self.logger.info("Public key saved to %s", public_key_path)

        route_paths = (
            route.resource.canonical for route in self.hass.http.app.router.routes()
        )
        public_key_route = "/.well-known/appspecific/com.tesla.3p.public-key.pem"
        if public_key_route not in route_paths:
            self.logger.info("Registering PEM endpoint")
            await self.hass.http.async_register_static_paths(
                [
                    StaticPathConfig(
                        public_key_route,
                        public_key_path,
                        cache_headers=False,
                    )
                ]
            )

        external_url = self.hass.config.external_url
        default_domain = None
        if external_url:
            try:
                parsed_url_object = urlparse(external_url)
                if parsed_url_object.hostname:
                    default_domain = parsed_url_object.hostname
            except ValueError:
                pass

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_CLIENT_ID,
                        msg="Your Tesla app's client ID.",
                    ): str,
                    vol.Required(
                        CONF_CLIENT_SECRET,
                        msg="Your Tesla app's client secret.",
                    ): str,
                    vol.Required(
                        CONF_INSTANCE_DOMAIN,
                        msg="The publicly accessible domain your Home Assistant is hosted on.",
                        default=default_domain,
                    ): str,
                    vol.Required(
                        CONF_AUDENCE,
                        msg="Base URL for Tesla API for your region.",
                        default=AUDIENCE_DEFAULT,
                    ): str,
                }
            ),
            errors=errors,
            description_placeholders=placeholders,
        )

    async def register_tesla_app(
        self, user_input: dict[str, str]
    ) -> tuple[str | None, dict[str, str]]:
        """Register the Tesla app with the Fleet API."""
        client_id = user_input[CONF_CLIENT_ID]
        client_secret = user_input[CONF_CLIENT_SECRET]
        ha_instance_domain = user_input[CONF_INSTANCE_DOMAIN]
        api_audience = user_input[CONF_AUDENCE]

        session = async_get_clientsession(self.hass)
        access_token = None

        try:
            self.logger.info("Requesting client credentials token")
            async with session.post(
                "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token",
                data={
                    "grant_type": "client_credentials",
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "scope": (
                        "openid offline_access user_data vehicle_device_data"
                        " vehicle_location vehicle_cmds vehicle_charging_cmds"
                        " energy_device_data energy_cmds"
                    ),
                    "audience": api_audience,
                },
            ) as response:
                if response.status in (400, 401, 403):
                    return "invalid_app_credentials", {}
                if response.status >= 400:
                    self.logger.error(
                        "POST /oauth2/v3/token failed with %s - %s: %s",
                        response.status,
                        response.reason,
                        await response.text(),
                    )
                    return "token_request_failed", {
                        "status": str(response.status),
                        "status_text": response.reason,
                        "response": await response.text(),
                    }
                body = await response.json()
                access_token = body.get("access_token")
                if not access_token:
                    self.logger.error(
                        "Access token not found in Tesla API response: %s",
                        await response.text(),
                    )
                    return "token_missing", {}
        except aiohttp.ClientError as err:
            self.logger.error(
                "Network error requesting client credentials token: %s", err
            )
            return "token_network_error", {}
        except Exception:  # pylint: disable=broad-except
            self.logger.exception(
                "Unexpected error requesting client credentials token"
            )
            return "unknown_error_token", {}

        try:
            self.logger.info("Registering partner account")
            async with session.post(
                url=f"{api_audience.rstrip('/')}/api/1/partner_accounts",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                },
                json={"domain": ha_instance_domain},
            ) as response:
                if response.status >= 400:
                    self.logger.error(
                        "POST /api/1/partner_accounts failed with %s %s: %s",
                        response.status,
                        response.reason,
                        await response.text(),
                    )
                    return "registration_failed", {
                        "status": str(response.status),
                        "status_text": response.reason,
                        "response": await response.text(),
                    }
                self.logger.info(
                    "Partner account registration successful for domain: %s",
                    ha_instance_domain,
                )
        except aiohttp.ClientError as err:
            self.logger.error("Network error registering partner account: %s", err)
            return "registration_network_error", {}
        except Exception:  # pylint: disable=broad-except
            self.logger.exception("Unexpected error registering partner account")
            return "unknown_error_register", {}

        # Store/Update credentials in Application Credentials
        app_cred_storage: ApplicationCredentialsStorageCollection = self.hass.data.get(
            APPLICATION_CREDENTIALS_DOMAIN
        )
        if not app_cred_storage:
            self.logger.error("Application credentials component not loaded")
            return "app_cred_not_loaded", {}

        auth_identifier = f"{DOMAIN}.{client_id}"
        found_matching_credential = False

        for item_id, item_data in app_cred_storage.data.items():
            if (
                item_data.get(CONF_DOMAIN) == DOMAIN
                and item_data.get(CONF_CLIENT_ID) == client_id
            ):
                if (
                    item_data.get(CONF_CLIENT_SECRET) == client_secret
                    and item_data.get(CONF_INSTANCE_DOMAIN) == ha_instance_domain
                    and item_data.get(CONF_AUTH_DOMAIN) == auth_identifier
                ):
                    found_matching_credential = True
                else:
                    self.logger.info(
                        "Found existing application credential for client_id %s with a different config. It will be replaced",
                        client_id,
                    )
                    try:
                        await app_cred_storage.async_delete_item(item_id)
                        self.logger.info(
                            "Deleted old application credential %s", item_id
                        )
                    except HomeAssistantError as e:
                        self.logger.error(
                            "Failed to delete old application credential %s: %s",
                            item_id,
                            e,
                        )
                        return "credential_deletion_failed", {}
                break

        if not found_matching_credential:
            try:
                await app_cred_storage.async_create_item(
                    {
                        CONF_DOMAIN: DOMAIN,
                        CONF_INSTANCE_DOMAIN: ha_instance_domain,
                        CONF_CLIENT_ID: client_id,
                        CONF_CLIENT_SECRET: client_secret,
                        CONF_AUTH_DOMAIN: auth_identifier,
                        CONF_NAME: f"Tesla Fleet ({client_id[:8]})",
                    }
                )
                self.logger.info(
                    "Created new application credential with auth_domain: %s",
                    auth_identifier,
                )
            except (vol.Invalid, HomeAssistantError) as err:
                self.logger.error("Failed to create application credential: %s", err)
                return "credential_creation_failed", {}

        self.logger.info(
            "Application registration successful, proceeding to OAuth2 user authorization"
        )
        return None, {}

    async def async_oauth_create_entry(
        self,
        data: dict[str, Any],
    ) -> ConfigFlowResult:
        """Handle the initial step."""

        token = jwt.decode(
            data["token"]["access_token"], options={"verify_signature": False}
        )
        uid = token["sub"]

        await self.async_set_unique_id(uid)
        if self.source == SOURCE_REAUTH:
            self._abort_if_unique_id_mismatch(reason="reauth_account_mismatch")
            return self.async_update_reload_and_abort(
                self._get_reauth_entry(), data=data
            )
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title=uid, data=data)

    async def async_step_reauth(
        self, entry_data: Mapping[str, Any]
    ) -> ConfigFlowResult:
        """Perform reauth upon an API authentication error."""
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm reauth dialog."""
        if user_input is None:
            return self.async_show_form(
                step_id="reauth_confirm",
                description_placeholders={"name": "Tesla Fleet push"},
            )
        return await self.async_step_user()
