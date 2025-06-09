"""The De'Longhi DDSX Dehumidifier (based on Ayla IOT) integration."""

from __future__ import annotations

from contextlib import suppress

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import aiohttp_client

from .ayla_iot_unofficial import new_ayla_api
from .const import (
    API_TIMEOUT,
    COMFORT_APP_ID,
    COMFORT_APP_SECRET,
    CONF_EUROPE,
    CONF_REGION,
    REGION_DEFAULT,
    REGION_EU,
)
from .coordinator import DelonghiCoordinator

PLATFORMS: list[Platform] = [
    Platform.HUMIDIFIER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry[DelonghiCoordinator]
) -> bool:
    """Set up De'Longhi DDSX Dehumidifier (based on Ayla IOT) from a config entry."""
    api = new_ayla_api(
        None,
        None,
        COMFORT_APP_ID,
        COMFORT_APP_SECRET,
        europe=entry.data[CONF_REGION] == REGION_EU,
        websession=aiohttp_client.async_get_clientsession(hass),
        timeout=API_TIMEOUT,
        token=entry.data[CONF_ACCESS_TOKEN],
    )

    coordinator = DelonghiCoordinator(hass, entry, api)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(
    hass: HomeAssistant, entry: ConfigEntry[DelonghiCoordinator]
) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    with suppress(TimeoutError):
        await entry.runtime_data.api.async_sign_out()

    return unload_ok


async def async_migrate_entry(
    hass: HomeAssistant, entry: ConfigEntry[DelonghiCoordinator]
) -> bool:
    """Migrate old entry."""
    if entry.version > 1:
        return False

    if entry.version == 1:
        new_data = {**entry.data}
        if entry.minor_version < 2:
            is_europe = new_data.get(CONF_EUROPE, False)
            if is_europe:
                new_data[CONF_REGION] = REGION_EU
            else:
                new_data[CONF_REGION] = REGION_DEFAULT

        hass.config_entries.async_update_entry(
            entry, data=new_data, minor_version=2, version=1
        )

    return True
