"""Support for De'Longhi DDSX dehumidifiers."""

from __future__ import annotations

from typing import Any

from homeassistant.components.humidifier import HumidifierAction, HumidifierEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .coordinator import DelonghiCoordinator
from .entity import DelonghiDehumidifierEntity
from .properties import (
    DEVICE_MODE_AIR_FILTRATION,
    DEVICE_STATUS_ACTIVE,
    STATUS_OFF,
    STATUS_ON,
    PropKey,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[DelonghiCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up dehumidifier dynamically."""
    coordinator = entry.runtime_data
    devices = coordinator.data.values()
    async_add_entities(DelonghiDehumidifier(coordinator, device) for device in devices)


class DelonghiDehumidifier(DelonghiDehumidifierEntity, HumidifierEntity):
    """Representation of a De'Longhi dehumidifier."""

    @property
    def available(self) -> bool:
        """Return if the device is available."""
        return super().available and self.coordinator_context in self.coordinator.data

    @property
    def is_on(self) -> bool:
        """Return whether the device is on or off."""
        return self.device.property_values.get(PropKey.STATUS, STATUS_OFF) == STATUS_ON

    @property
    def action(self) -> HumidifierAction | None:
        """Return current action."""
        if not self.is_on:
            return HumidifierAction.OFF
        props = self.device.property_values
        if (
            props.get(PropKey.DEVICE_STATUS) == DEVICE_STATUS_ACTIVE
            and props.get(PropKey.DEVICE_MODE) != DEVICE_MODE_AIR_FILTRATION
            and props.get(PropKey.CURRENT_SPEED, 0) > 0
        ):
            return HumidifierAction.DRYING
        return HumidifierAction.IDLE

    @property
    def target_humidity(self) -> float | None:
        """Return the humidity we try to reach."""
        return self.device.property_values.get(PropKey.HUMIDITY_SETPOINT, 0.0)

    @property
    def current_humidity(self) -> float | None:
        """Return the current humidity."""
        return self.device.property_values.get(PropKey.CURRENT_HUMIDITY, 0.0)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the device on."""
        await self.device.async_set_property_value(PropKey.STATUS, STATUS_ON)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the device off."""
        await self.device.async_set_property_value(PropKey.STATUS, STATUS_OFF)
        await self.coordinator.async_request_refresh()

    async def async_set_humidity(self, humidity: float) -> None:
        """Set new target humidity."""
        await self.device.async_set_property_value(PropKey.HUMIDITY_SETPOINT, humidity)
        await self.coordinator.async_request_refresh()
