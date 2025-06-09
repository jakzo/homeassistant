"""Sensors for De'Longhi DDSX Dehumidifier."""

from collections.abc import Mapping
from typing import Any

from homeassistant.components.sensor import (
    EntityCategory,
    SensorDeviceClass,
    SensorEntity,
    StateType,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .ayla_iot_unofficial.device import Device
from .coordinator import DelonghiCoordinator
from .entity import DelonghiDehumidifierEntity
from .properties import PROPERTIES, UNKNOWN, DataKey, is_property_switch


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[DelonghiCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up sensors for De'Longhi DDSX Dehumidifier device."""
    coordinator = entry.runtime_data
    async_add_entities(
        DelonghiPropertySensor(coordinator, device, prop_key)
        for device in coordinator.data.values()
        for prop_key, prop_data in device.properties_full.items()
        if not is_property_switch(prop_data)
    )


class DelonghiPropertySensor(DelonghiDehumidifierEntity, SensorEntity):
    """Entity representing a property of the De'Longhi Dehumidifier."""

    def __init__(
        self,
        coordinator: DelonghiCoordinator,
        device: Device,
        property_key: str,
    ) -> None:
        """Initialize the property sensor."""
        super().__init__(coordinator, device)
        self.property_key = property_key
        prop_data = device.properties_full[property_key]
        self.property = PROPERTIES.get(property_key)

        self._attr_name = (
            self.property.name
            if self.property and self.property.name
            else prop_data.get(DataKey.DISPLAY_NAME, property_key)
        )
        self._attr_unique_id = f"{device.device_serial_number}_{property_key}"

        if self.property and self.property.options:
            self.options = [prop.name for prop in self.property.options.values()]
            self._attr_device_class = SensorDeviceClass.ENUM
            self._attr_options = [
                *(prop.name for prop in self.property.options.values()),
                UNKNOWN,
            ]

        self._attr_entity_category = (
            self.property.entity_category
            if self.property and self.property.entity_category
            else EntityCategory.DIAGNOSTIC
        )

    @property
    def native_value(self) -> StateType:
        """Return the value of the property."""
        value = (
            self.property.current_value(self.device)
            if self.property and self.property.current_value
            else self.device.property_values[self.property_key]
        )
        if self.property and self.property.options:
            option = self.property.options.get(value)
            return option.name if option else UNKNOWN
        # Max state length is 255 chars
        if isinstance(value, str) and len(value) > 255:
            return value[:255]
        return value

    @property
    def icon(self) -> str | None:
        """Return the icon to use in the frontend, if any."""
        if self.property:
            if self.property.options:
                option = self.property.options.get(
                    self.device.property_values[self.property_key]
                )
                if option and option.icon:
                    return option.icon
            if self.property.icon:
                return self.property.icon
        return "mdi:card-text-outline"

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        """Return the state attributes."""
        return self.device.properties_full.get(self.property_key)
