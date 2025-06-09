"""Tesla Fleet push integration."""

import asyncio
from typing import Final

from aiohttp import web
from aiohttp.client_exceptions import ClientResponseError
import jwt

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_TOKEN, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import (
    OAuth2Session,
    async_get_config_entry_implementation,
)
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, LOGGER, MODELS
from .coordinator import TeslaFleetVehicleDataCoordinator
from .models import TeslaFleetData, TeslaFleetVehicleData
from .tesla_fleet_api import TeslaFleetApi, VehicleSigned, VehicleSpecific
from .tesla_fleet_api.const import Scope
from .tesla_fleet_api.exceptions import (
    InvalidRegion,
    InvalidToken,
    LibraryError,
    LoginRequired,
    OAuthExpired,
    TeslaFleetError,
)

PLATFORMS: Final = [
    Platform.SENSOR,
]

type TeslaFleetConfigEntry = ConfigEntry[TeslaFleetData]

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


async def async_setup_entry(hass: HomeAssistant, entry: TeslaFleetConfigEntry) -> bool:
    """Set up TeslaFleet config."""

    try:
        implementation = await async_get_config_entry_implementation(hass, entry)
    except ValueError as e:
        # Remove invalid implementation from config entry then raise AuthFailed
        hass.config_entries.async_update_entry(
            entry, data={"auth_implementation": None}
        )
        raise ConfigEntryAuthFailed from e

    access_token = entry.data[CONF_TOKEN][CONF_ACCESS_TOKEN]
    session = async_get_clientsession(hass)

    token = jwt.decode(access_token, options={"verify_signature": False})
    scopes: list[Scope] = [Scope(s) for s in token["scp"]]
    region: str = token["ou_code"].lower()

    oauth_session = OAuth2Session(hass, entry, implementation)
    refresh_lock = asyncio.Lock()

    async def _refresh_token() -> str:
        async with refresh_lock:
            try:
                await oauth_session.async_ensure_token_valid()
            except ClientResponseError as e:
                if e.status == 401:
                    raise ConfigEntryAuthFailed from e
                raise ConfigEntryNotReady from e
            token: str = oauth_session.token[CONF_ACCESS_TOKEN]
            return token

    # Create API connection
    tesla = TeslaFleetApi(
        session=session,
        access_token=access_token,
        region=region,
        charging_scope=False,
        partner_scope=False,
        energy_scope=Scope.ENERGY_DEVICE_DATA in scopes,
        vehicle_scope=Scope.VEHICLE_DEVICE_DATA in scopes,
        refresh_hook=_refresh_token,
    )
    try:
        products = (await tesla.products())["response"]
    except (InvalidToken, OAuthExpired, LoginRequired) as e:
        raise ConfigEntryAuthFailed from e
    except InvalidRegion:
        try:
            LOGGER.warning("Region is invalid, trying to find the correct region")
            await tesla.find_server()
            try:
                products = (await tesla.products())["response"]
            except TeslaFleetError as e:
                raise ConfigEntryNotReady from e
        except LibraryError as e:
            raise ConfigEntryAuthFailed from e
    except TeslaFleetError as e:
        raise ConfigEntryNotReady from e

    # Create array of classes
    vehicles: list[TeslaFleetVehicleData] = []
    for product in products:
        if "vin" in product and hasattr(tesla, "vehicle"):
            # Remove the protobuff 'cached_data' that we do not use to save memory
            product.pop("cached_data", None)
            vin = product["vin"]
            signing = product["command_signing"] == "required"
            if signing:
                if not tesla.private_key:
                    await tesla.get_private_key(hass.config.path("tesla_fleet.key"))
                api = VehicleSigned(tesla.vehicle, vin)
            else:
                api = VehicleSpecific(tesla.vehicle, vin)
            coordinator = TeslaFleetVehicleDataCoordinator(hass, entry, api, product)

            await coordinator.async_config_entry_first_refresh()

            device = DeviceInfo(
                identifiers={(DOMAIN, vin)},
                manufacturer="Tesla",
                name=product["display_name"],
                model=MODELS.get(vin[3]),
                serial_number=vin,
            )

            vehicles.append(
                TeslaFleetVehicleData(
                    api=api,
                    coordinator=coordinator,
                    vin=vin,
                    device=device,
                    signing=signing,
                )
            )

    async def push_endpoint_handler(request: web.Request) -> web.StreamResponse:
        """Handle a custom endpoint."""
        body = await request.text()
        LOGGER.info("Received push from Tesla: %s", body)
        return web.Response(
            content_type="application/json",
            text='{ "message": "Received" }',
        )

    hass.http.app.router.add_post(f"/{DOMAIN}/push", push_endpoint_handler)

    for vehicle in vehicles:
        try:
            vehicle_config = await vehicle.api.fleet_telemetry_config_get()
            LOGGER.debug(
                "Current telemetry config for %s: %s", vehicle.vin, vehicle_config
            )
            await vehicle.api.fleet_telemetry_config_create(
                {"endpoint": f"{hass.config.api.base_url}/{DOMAIN}/push"}
            )
        except TeslaFleetError as e:
            LOGGER.error("Failed to register push endpoint for %s: %s", vehicle.vin, e)
            raise ConfigEntryNotReady from e

    # Setup Platforms
    entry.runtime_data = TeslaFleetData(vehicles, scopes)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: TeslaFleetConfigEntry) -> bool:
    """Unload TeslaFleet Config."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
