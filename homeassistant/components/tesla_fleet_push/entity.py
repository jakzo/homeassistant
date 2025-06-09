"""Tesla Fleet parent entity class."""

from abc import abstractmethod
from typing import Any

from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import TeslaFleetVehicleDataCoordinator
from .helpers import wake_up_vehicle
from .models import TeslaFleetVehicleData
from .tesla_fleet_api import VehicleSpecific
from .tesla_fleet_api.const import Scope


class TeslaFleetEntity(CoordinatorEntity[TeslaFleetVehicleDataCoordinator]):
    """Parent class for all TeslaFleet entities."""

    _attr_has_entity_name = True
    read_only: bool
    scoped: bool

    def __init__(
        self,
        coordinator: TeslaFleetVehicleDataCoordinator,
        api: VehicleSpecific,
        key: str,
    ) -> None:
        """Initialize common aspects of a TeslaFleet entity."""
        super().__init__(coordinator)
        self.api = api
        self.key = key
        self._attr_translation_key = self.key
        self._async_update_attrs()

    @property
    def available(self) -> bool:
        """Return if sensor is available."""
        return self.coordinator.last_update_success and self._attr_available

    @property
    def _value(self) -> Any | None:
        """Return a specific value from coordinator data."""
        return self.coordinator.data.get(self.key)

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """Return a specific value from coordinator data."""
        return self.coordinator.data.get(key, default)

    def get_number(self, key: str, default: float) -> float:
        """Return a specific number from coordinator data."""
        if isinstance(value := self.coordinator.data.get(key), (int, float)):
            return value
        return default

    @property
    def is_none(self) -> bool:
        """Return if the value is a literal None."""
        return self.get(self.key, False) is None

    @property
    def has(self) -> bool:
        """Return True if a specific value is in coordinator data."""
        return self.key in self.coordinator.data

    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._async_update_attrs()
        self.async_write_ha_state()

    @abstractmethod
    def _async_update_attrs(self) -> None:
        """Update the attributes of the entity."""

    def raise_for_read_only(self, scope: Scope) -> None:
        """Raise an error if a scope is not available."""
        if not self.scoped:
            raise ServiceValidationError(
                translation_domain=DOMAIN,
                translation_key=f"missing_scope_{scope.name.lower()}",
            )


class TeslaFleetVehicleEntity(TeslaFleetEntity):
    """Parent class for TeslaFleet Vehicle entities."""

    _last_update: int = 0

    def __init__(
        self,
        data: TeslaFleetVehicleData,
        key: str,
    ) -> None:
        """Initialize common aspects of a Tesla Fleet entity."""

        self._attr_unique_id = f"{data.vin}-{key}"
        self.vehicle = data

        self._attr_device_info = data.device
        super().__init__(data.coordinator, data.api, key)

    @property
    def _value(self) -> Any | None:
        """Return a specific value from coordinator data."""
        return self.coordinator.data.get(self.key)

    async def wake_up_if_asleep(self) -> None:
        """Wake up the vehicle if its asleep."""
        await wake_up_vehicle(self.vehicle)
