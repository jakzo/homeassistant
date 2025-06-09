"""The Tesla Fleet integration models."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

from homeassistant.helpers.device_registry import DeviceInfo

from .coordinator import TeslaFleetVehicleDataCoordinator
from .tesla_fleet_api import VehicleSpecific
from .tesla_fleet_api.const import Scope


@dataclass
class TeslaFleetData:
    """Data for the TeslaFleet integration."""

    vehicles: list[TeslaFleetVehicleData]
    scopes: list[Scope]


@dataclass
class TeslaFleetVehicleData:
    """Data for a vehicle in the TeslaFleet integration."""

    api: VehicleSpecific
    coordinator: TeslaFleetVehicleDataCoordinator
    vin: str
    device: DeviceInfo
    signing: bool
    wakelock = asyncio.Lock()
