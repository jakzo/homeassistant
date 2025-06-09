"""Coordinator for De'Longhi DDSX Dehumidifier integration."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .ayla_iot_unofficial import AylaApi, AylaAuthError
from .ayla_iot_unofficial.device import Device
from .const import API_REFRESH

_LOGGER = logging.getLogger(__name__)

type DelonghiConfig = ConfigEntry[DelonghiCoordinator]


class DelonghiCoordinator(DataUpdateCoordinator[dict[str, Device]]):
    """Coordinator for De'Longhi DDSX Dehumidifier integration."""

    config_entry: DelonghiConfig

    def __init__(
        self, hass: HomeAssistant, config_entry: DelonghiConfig, api: AylaApi
    ) -> None:
        """Initialize coordinator for De'Longhi DDSX Dehumidifier integration."""
        super().__init__(
            hass,
            _LOGGER,
            config_entry=config_entry,
            name="De'Longhi DDSX Dehumidifier data",
            update_interval=API_REFRESH,
        )
        self.api = api

    async def _async_setup(self) -> None:
        try:
            await self.api.async_sign_in()
        except AylaAuthError as e:
            raise ConfigEntryAuthFailed("Credentials expired for Ayla IoT API") from e

    async def _async_update_data(self) -> dict[str, Device]:
        """Fetch data from api endpoint."""
        listening_entities = set(self.async_contexts())
        try:
            # TODO: Shouldn't we try refreshing first?
            # TODO: Save refresh token for use after restart?
            if self.api.token_expired:
                await self.api.async_sign_in()

            if self.api.token_expiring_soon:
                await self.api.async_refresh_auth()

            devices = await self.api.async_get_devices()
        except AylaAuthError as e:
            raise ConfigEntryAuthFailed("Credentials expired for Ayla IoT API") from e

        if listening_entities:
            devices = [
                dev for dev in devices if dev.device_serial_number in listening_entities
            ]

        try:
            for dev in devices:
                await dev.async_update()
        except AylaAuthError as e:
            raise ConfigEntryAuthFailed("Credentials expired for Ayla IoT API") from e

        return {d.device_serial_number: d for d in devices}
