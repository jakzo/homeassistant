"""De'Longhi DDSX dehumidifier property definitions."""

# Sample properties:
# "room_temp": 250,
# "activate_realfeel": "AAIDChIXHEY8Mig=",
# "activate_schedule": False,
# "alarm_state": 3,
# "appliance": "Dehumidifiers",
# "appliance_category": "HVAC Category",
# "appliance_model": "DDSX220",
# "color": None,
# "current_humidity": 81.0,
# "current_speed": 0,
# "device_mode": 1,
# "device_status": 3,
# "eco": False,
# "filter_change_alarm": False,
# "filter_life": 458960,
# "filter_reset": None,
# "filter_status": True,
# "firmware_version": "1.0",
# "hardware_version": "1.0",
# "heat_exchanger_temp": 240,
# "humidity_setpoint": 55.0,
# "mcu_host_version": "1.9.8-B2",
# "rotation_speed": 3,
# "schedule": "RLEwAADIAGQTEFVQAAAAAFVQAAAAAFVQAAAAAFVQAAAAAFVQAAAAAFVQAAAAAFVQAAAAAA==",
# "serial_number": "DUMMY__DUMMY",
# "software_version": "DL_humidifier_demo 1.9.8-B2 May 27 2022 16:26:02",
# "status": 1,
# "status_history": "8HLmZ2oBPDc0NzQ3NDc0NzQ3NDc0NzQ3NDc0NzQ3ODc4N7k3uTe5N7k3tje5N6w3pDewN7M3tTe3N7g3uTezN7M3tTe3N7Y3uTe1N7M3szezN7Q3uje1N7U3uDezN7g3tTe4N7U3tje4N7c3tze2N7U3tTe3N7M3tTe1N7U3tTe1N7Y3tje1N7U3uTe3N7g3tTe2N0Y3TTdGN0c3RzdIN0g3SDdKN0s3TDdON083TzdQN083RzdKN0o3SDdJN0o3SzdMN003TjdNN083TjdON043UDdRN1I3UTdSN1M3UjdRN1A3UTdQN1E3UTdSN1E3UTdSN1E3UTdRN083TjdON043TzdQN1A3UTdSN1I3UzdUN1U3VDdTN1I3STdLN0w3TTdON083UDdRN9E3RjdaN1g3UzdVN1Q3UzdUN1c3QTdON1A3TzdNN043TzdQN1E3UjdSN1Q3VTdWN1c3WTdZN1o3WjdZN1g3VzdVN1I3UTc=",
# "swing": True,
# "temp_unit": None,
# "voice1": "Spare room",
# "voice2": None,

from collections.abc import Callable
from enum import StrEnum
from typing import Any

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    EntityCategory,
    UnitOfTemperature,
    UnitOfTime,
)

from .ayla_iot_unofficial.device import Device


class PropertyOption:
    """Ayla property option."""

    def __init__(self, name: str, icon: str | None = None) -> None:
        """Initialize the property option."""
        self.name = name
        self.icon = icon


class Property:
    """Ayla property."""

    def __init__(
        self,
        name: str | None = None,
        icon: str | None = None,
        device_class: SensorDeviceClass | None = None,
        native_unit_of_measurement: str | None = None,
        suggested_display_precision: int | None = None,
        state_class: SensorStateClass | None = None,
        entity_category: EntityCategory | None = None,
        available: Callable[[Device], bool] | None = None,
        current_value: Callable[[Device], Any] | None = None,
        options: dict[int, PropertyOption] | None = None,
    ) -> None:
        """Initialize the property."""
        self.name = name
        self.icon = icon
        self.device_class = device_class
        self.native_unit_of_measurement = native_unit_of_measurement
        self.suggested_display_precision = suggested_display_precision
        self.state_class = state_class
        self.entity_category = entity_category
        self.available = available
        self.current_value = current_value
        self.options = options


class PropKey(StrEnum):
    """De'Longhi DDSX dehumidifier property keys."""

    # Sensors
    ROOM_TEMP = "room_temp"
    HEAT_EXCHANGER_TEMP = "heat_exchanger_temp"
    CURRENT_SPEED = "current_speed"
    DEVICE_STATUS = "device_status"
    ALARM_STATE = "alarm_state"
    CURRENT_HUMIDITY = "current_humidity"
    HUMIDITY_SETPOINT = "humidity_setpoint"
    FILTER_LIFE = "filter_life"

    # Switches
    STATUS = "status"
    ACTIVATE_SCHEDULE = "activate_schedule"
    FILTER_RESET = "filter_reset"
    SWING = "swing"
    ECO = "eco"

    # Selects
    DEVICE_MODE = "device_mode"
    ROTATION_SPEED = "rotation_speed"


class DataKey(StrEnum):
    """De'Longhi DDSX dehumidifier property data keys."""

    DISPLAY_NAME = "display_name"
    DIRECTION = "direction"
    BASE_TYPE = "base_type"


UNKNOWN = "Unknown"

STATUS_ON = 1
STATUS_OFF = 2

DEVICE_MODE_DEHUMIDIFY = 1
DEVICE_MODE_AIR_FILTRATION = 3
DEVICE_MODE_REALFEEL = 4

DEVICE_STATUS_ACTIVE = 1

FAN_SPEED_OPTIONS: dict[int, PropertyOption] = {
    0: PropertyOption("Off", icon="mdi:fan"),
    1: PropertyOption("Low", icon="mdi:fan"),
    2: PropertyOption("Medium", icon="mdi:fan"),
    3: PropertyOption("High", icon="mdi:fan"),
}

DIRECTION_INPUT = "input"

# TODO: filter_status, filter_change_alarm, schedule
PROPERTIES: dict[str, Property] = {
    # TODO: How is temp_unit used and does it change these values?
    PropKey.ROOM_TEMP: Property(
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        state_class=SensorStateClass.MEASUREMENT,
        current_value=lambda device: device.property_values[PropKey.ROOM_TEMP] / 10.0,
    ),
    PropKey.HEAT_EXCHANGER_TEMP: Property(
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        state_class=SensorStateClass.MEASUREMENT,
        current_value=lambda device: device.property_values[PropKey.HEAT_EXCHANGER_TEMP]
        / 10.0,
    ),
    PropKey.CURRENT_SPEED: Property(
        name="Current Fan Speed",
        icon="mdi:fan",
        options=FAN_SPEED_OPTIONS,
    ),
    PropKey.DEVICE_STATUS: Property(
        icon="mdi:air-humidifier",
        options={
            DEVICE_STATUS_ACTIVE: PropertyOption("Active", icon="mdi:air-humidifier"),
            2: PropertyOption("Off", icon="mdi:power-off"),
            3: PropertyOption("Tank full", icon="mdi:beaker"),
        },
    ),
    PropKey.ALARM_STATE: Property(
        icon="mdi:check",
        options={
            0: PropertyOption("Normal", icon="mdi:check"),
            3: PropertyOption("Tank full", icon="mdi:beaker-alert"),
            5: PropertyOption("Change filter", icon="mdi:clock-alert"),
        },
    ),
    PropKey.CURRENT_HUMIDITY: Property(
        icon="mdi:water-percent",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    PropKey.HUMIDITY_SETPOINT: Property(
        icon="mdi:water-percent",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    # TODO: What is filter_life measuring?
    PropKey.FILTER_LIFE: Property(
        icon="mdi:progress-clock",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    PropKey.STATUS: Property(
        name="Power",
        icon="mdi:power",
    ),
    PropKey.ACTIVATE_SCHEDULE: Property(
        icon="mdi:calendar-clock",
        available=lambda device: device.property_values.get(
            PropKey.DEVICE_MODE, DEVICE_MODE_REALFEEL
        )
        != DEVICE_MODE_REALFEEL,
    ),
    # TODO: How is filter reset meant to be used?
    PropKey.FILTER_RESET: Property(
        icon="mdi:grid",
    ),
    PropKey.SWING: Property(
        icon="mdi:arrow-up-down",
    ),
    PropKey.ECO: Property(
        name="Eco Mode",
        icon="mdi:leaf",
        available=lambda device: device.property_values.get(PropKey.DEVICE_MODE)
        == DEVICE_MODE_DEHUMIDIFY,
    ),
    PropKey.DEVICE_MODE: Property(
        icon="mdi:air-humidifier",
        options={
            DEVICE_MODE_DEHUMIDIFY: PropertyOption("Dehumidify", icon="mdi:water"),
            2: PropertyOption("Dry", icon="mdi:tshirt-crew-outline"),
            DEVICE_MODE_AIR_FILTRATION: PropertyOption(
                "Air filtration", icon="mdi:air-filter"
            ),
            DEVICE_MODE_REALFEEL: PropertyOption("RealFeel", icon="mdi:auto-fix"),
        },
    ),
    # TODO: Bug with rotation speed (fan speed) when changing modes, it keeps the current fan speed (ie. 3 when in dry mode) and DOES NOT change fan speed in the device to what Ayla reports. We should change fan speed as well after changing modes.
    PropKey.ROTATION_SPEED: Property(
        name="Fan Speed Setting",
        icon="mdi:fan",
        available=lambda device: device.property_values.get(PropKey.DEVICE_MODE)
        == DEVICE_MODE_AIR_FILTRATION,
        # When switching modes the set fan speed is not updated so show the current speed instead
        current_value=lambda device: device.property_values.get(
            PropKey.CURRENT_SPEED, device.property_values[PropKey.ROTATION_SPEED]
        ),
        options=FAN_SPEED_OPTIONS,
    ),
}


def is_property_switch(prop_data: dict) -> bool:
    """Return True if the property is a switch."""
    return (
        prop_data[DataKey.DIRECTION] == DIRECTION_INPUT
        and prop_data[DataKey.BASE_TYPE] == "boolean"
    )


def is_property_select(prop_key: str, prop_data: dict) -> bool:
    """Return True if the property is a select."""
    prop = PROPERTIES.get(prop_key)
    return (
        prop
        and prop.options
        and prop_data[DataKey.DIRECTION] == DIRECTION_INPUT
        and prop_data[DataKey.BASE_TYPE] == "integer"
    )
