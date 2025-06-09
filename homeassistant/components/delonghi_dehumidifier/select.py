"""Sensors for De'Longhi DDSX Dehumidifier."""

from homeassistant.components.select import SelectEntity
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
    is_property_select,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[DelonghiCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up sensors for De'Longhi DDSX Dehumidifier device."""
    coordinator = entry.runtime_data
    async_add_entities(
        DelonghiPropertySelect(coordinator, device, prop_key)
        for device in coordinator.data.values()
        for prop_key, prop_data in device.properties_full.items()
        if is_property_select(prop_key, prop_data)
    )


class DelonghiPropertySelect(DelonghiDehumidifierEntity, SelectEntity):
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
        if not self.property:
            raise ValueError(f"Unrecognized property key: {property_key}")
        if not self.property.options:
            raise ValueError(f"Property missing options: {property_key}")

        self._attr_name = self.property.name or prop_data.get(
            DataKey.DISPLAY_NAME, property_key
        )
        self._attr_unique_id = f"{device.device_serial_number}_{property_key}"
        self.options = [prop.name for prop in self.property.options.values()]
        self._option_values_by_name = {
            prop.name: value for value, prop in self.property.options.items()
        }

    @property
    def current_option(self) -> str | None:
        """Return the value of the property."""
        value = (
            self.property.current_value(self.device)
            if self.property.current_value
            else self.device.property_values[self.property_key]
        )
        option = self.property.options.get(value)
        return option.name if option else str(value)

    @property
    def icon(self) -> str | None:
        """Return the icon to use in the frontend, if any."""
        value = self.device.property_values[self.property_key]
        option = self.property.options.get(value)
        return option.icon if option and option.icon else self.property.icon

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if self.device.property_values[PropKey.DEVICE_STATUS] != DEVICE_STATUS_ACTIVE:
            return False
        if self.property.available:
            return self.property.available(self.device)
        return super().available

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        value = self._option_values_by_name.get(option)
        if value is None:
            raise ValueError(f"Invalid option: {option}")
        await self.device.async_set_property_value(self.property_key, value)
        await self.coordinator.async_request_refresh()
