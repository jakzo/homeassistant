"""De'Longhi dehumidifier base entity."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .ayla_iot_unofficial.device import Device
from .const import DOMAIN
from .coordinator import DelonghiCoordinator


class DelonghiDehumidifierEntity(CoordinatorEntity[DelonghiCoordinator]):
    """Generic dehumidifier entity (base class)."""

    def __init__(self, coordinator: DelonghiCoordinator, device: Device) -> None:
        """Store the representation of the device."""
        super().__init__(coordinator, context=device.device_serial_number)

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.device_serial_number)},
            name=device.name,
            manufacturer="De'Longhi",
            model=device.property_values["appliance_model"],
            model_id=device.device_model_number,
            serial_number=device.device_serial_number,
            sw_version=device.property_values["mcu_host_version"],
            hw_version=device.property_values["hardware_version"],
        )
        self._attr_unique_id = device.device_serial_number
        self._attr_has_entity_name = True
        self._attr_name = device.name

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return super().available and self.coordinator_context in self.coordinator.data

    @property
    def device(self) -> Device:
        """Return the device object from the coordinator data."""
        return self.coordinator.data[self.coordinator_context]
