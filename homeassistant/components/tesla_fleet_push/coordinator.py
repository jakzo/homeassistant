"""Tesla Fleet Data Coordinator."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .tesla_fleet_api import VehicleSpecific
from .tesla_fleet_api.const import VehicleDataEndpoint

if TYPE_CHECKING:
    from . import TeslaFleetConfigEntry

from .const import LOGGER

VEHICLE_INTERVAL_SECONDS = 300
VEHICLE_INTERVAL = timedelta(seconds=VEHICLE_INTERVAL_SECONDS)
VEHICLE_WAIT = timedelta(minutes=15)

ENERGY_INTERVAL_SECONDS = 60
ENERGY_INTERVAL = timedelta(seconds=ENERGY_INTERVAL_SECONDS)
ENERGY_HISTORY_INTERVAL = timedelta(minutes=5)

ENDPOINTS = [
    VehicleDataEndpoint.CHARGE_STATE,
    VehicleDataEndpoint.CLIMATE_STATE,
    VehicleDataEndpoint.DRIVE_STATE,
    VehicleDataEndpoint.LOCATION_DATA,
    VehicleDataEndpoint.VEHICLE_STATE,
    VehicleDataEndpoint.VEHICLE_CONFIG,
]


def flatten(data: dict[str, Any], parent: str | None = None) -> dict[str, Any]:
    """Flatten the data structure."""
    result = {}
    for key, value in data.items():
        if parent:
            key = f"{parent}_{key}"
        if isinstance(value, dict):
            result.update(flatten(value, key))
        else:
            result[key] = value
    return result


class TeslaFleetVehicleDataCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Class to manage fetching data from the TeslaFleet API."""

    config_entry: TeslaFleetConfigEntry
    updated_once: bool
    pre2021: bool
    last_active: datetime

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: TeslaFleetConfigEntry,
        api: VehicleSpecific,
        product: dict,
    ) -> None:
        """Initialize TeslaFleet Vehicle Update Coordinator."""
        super().__init__(
            hass,
            LOGGER,
            config_entry=config_entry,
            name="Tesla Fleet Vehicle",
            update_interval=VEHICLE_INTERVAL,
        )
        self.api = api
        self.data = flatten(product)
        self.updated_once = False
        self.last_active = datetime.now()
