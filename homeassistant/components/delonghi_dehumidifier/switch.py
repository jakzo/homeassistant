"""Switches for De'Longhi DDSX Dehumidifier."""

from collections.abc import Mapping
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .ayla_iot_unofficial.device import Device
from .coordinator import DelonghiCoordinator
from .entity import DelonghiDehumidifierEntity
from .properties import (
    DEVICE_STATUS_ACTIVE,
    PROPERTIES,
    DataKey,
    PropKey,
    is_property_switch,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[DelonghiCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up switches for De'Longhi DDSX Dehumidifier device."""
    coordinator = entry.runtime_data
    async_add_entities(
        DelonghiPropertySwitch(coordinator, device, prop_key)
        for device in coordinator.data.values()
        for prop_key, prop_data in device.properties_full.items()
        if is_property_switch(prop_data)
    )


class DelonghiPropertySwitch(DelonghiDehumidifierEntity, SwitchEntity):
    """Entity representing a property of the De'Longhi Dehumidifier."""

    def __init__(
        self,
        coordinator: DelonghiCoordinator,
        device: Device,
        property_key: str,
    ) -> None:
        """Initialize the property switch."""
        super().__init__(coordinator, device)
        self.property_key = property_key
        prop_data = device.properties_full[property_key]
        self.property = PROPERTIES.get(property_key)
        self._attr_name = getattr(self.property, "name", None) or prop_data.get(
            DataKey.DISPLAY_NAME, property_key
        )
        self._attr_unique_id = f"{device.device_serial_number}_{property_key}"

    @property
    def icon(self) -> str | None:
        """Return the icon to use in the frontend, if any."""
        return getattr(self.property, "icon", None)

    @property
    def is_on(self) -> bool | None:
        """Return the value of the property."""
        return self.device.property_values.get(self.property_key)

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        """Return the state attributes."""
        return self.device.properties_full.get(self.property_key)

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if self.device.property_values[PropKey.DEVICE_STATUS] != DEVICE_STATUS_ACTIVE:
            return False
        if self.property.available:
            return self.property.available(self.device)
        return super().available

    def turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        self.device.set_property_value(self.property_key, 1)
        self.coordinator.async_request_refresh()

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        await self.device.async_set_property_value(self.property_key, 1)
        await self.coordinator.async_request_refresh()

    def turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        self.device.set_property_value(self.property_key, 0)
        self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        await self.device.async_set_property_value(self.property_key, 0)
        await self.coordinator.async_request_refresh()
