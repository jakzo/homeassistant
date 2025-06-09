from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar

import common_pb2 as _common_pb2
from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    timestamp_pb2 as _timestamp_pb2,
)
from google.protobuf.internal import (
    containers as _containers,
    enum_type_wrapper as _enum_type_wrapper,
)
import managed_charging_pb2 as _managed_charging_pb2
import vcsec_pb2 as _vcsec_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class MediaSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MediaSourceType_None: _ClassVar[MediaSourceType]
    MediaSourceType_AM: _ClassVar[MediaSourceType]
    MediaSourceType_FM: _ClassVar[MediaSourceType]
    MediaSourceType_XM: _ClassVar[MediaSourceType]
    MediaSourceType_Slacker: _ClassVar[MediaSourceType]
    MediaSourceType_LocalFiles: _ClassVar[MediaSourceType]
    MediaSourceType_iPod: _ClassVar[MediaSourceType]
    MediaSourceType_Bluetooth: _ClassVar[MediaSourceType]
    MediaSourceType_AuxIn: _ClassVar[MediaSourceType]
    MediaSourceType_DAB: _ClassVar[MediaSourceType]
    MediaSourceType_Rdio: _ClassVar[MediaSourceType]
    MediaSourceType_Spotify: _ClassVar[MediaSourceType]
    MediaSourceType_USRadio: _ClassVar[MediaSourceType]
    MediaSourceType_EURadio: _ClassVar[MediaSourceType]
    MediaSourceType_MediaFile: _ClassVar[MediaSourceType]
    MediaSourceType_TuneIn: _ClassVar[MediaSourceType]
    MediaSourceType_Stingray: _ClassVar[MediaSourceType]
    MediaSourceType_SiriusXM: _ClassVar[MediaSourceType]
    MediaSourceType_Tidal: _ClassVar[MediaSourceType]
    MediaSourceType_QQMusic: _ClassVar[MediaSourceType]
    MediaSourceType_QQMusic2: _ClassVar[MediaSourceType]
    MediaSourceType_Ximalaya: _ClassVar[MediaSourceType]
    MediaSourceType_OnlineRadio: _ClassVar[MediaSourceType]
    MediaSourceType_OnlineRadio2: _ClassVar[MediaSourceType]
    MediaSourceType_NetEaseMusic: _ClassVar[MediaSourceType]
    MediaSourceType_Browser: _ClassVar[MediaSourceType]
    MediaSourceType_Theater: _ClassVar[MediaSourceType]
    MediaSourceType_Game: _ClassVar[MediaSourceType]
    MediaSourceType_Tutorial: _ClassVar[MediaSourceType]
    MediaSourceType_Toybox: _ClassVar[MediaSourceType]
    MediaSourceType_RecentsFavorites: _ClassVar[MediaSourceType]
    MediaSourceType_HomeApps: _ClassVar[MediaSourceType]
    MediaSourceType_Search: _ClassVar[MediaSourceType]

MediaSourceType_None: MediaSourceType
MediaSourceType_AM: MediaSourceType
MediaSourceType_FM: MediaSourceType
MediaSourceType_XM: MediaSourceType
MediaSourceType_Slacker: MediaSourceType
MediaSourceType_LocalFiles: MediaSourceType
MediaSourceType_iPod: MediaSourceType
MediaSourceType_Bluetooth: MediaSourceType
MediaSourceType_AuxIn: MediaSourceType
MediaSourceType_DAB: MediaSourceType
MediaSourceType_Rdio: MediaSourceType
MediaSourceType_Spotify: MediaSourceType
MediaSourceType_USRadio: MediaSourceType
MediaSourceType_EURadio: MediaSourceType
MediaSourceType_MediaFile: MediaSourceType
MediaSourceType_TuneIn: MediaSourceType
MediaSourceType_Stingray: MediaSourceType
MediaSourceType_SiriusXM: MediaSourceType
MediaSourceType_Tidal: MediaSourceType
MediaSourceType_QQMusic: MediaSourceType
MediaSourceType_QQMusic2: MediaSourceType
MediaSourceType_Ximalaya: MediaSourceType
MediaSourceType_OnlineRadio: MediaSourceType
MediaSourceType_OnlineRadio2: MediaSourceType
MediaSourceType_NetEaseMusic: MediaSourceType
MediaSourceType_Browser: MediaSourceType
MediaSourceType_Theater: MediaSourceType
MediaSourceType_Game: MediaSourceType
MediaSourceType_Tutorial: MediaSourceType
MediaSourceType_Toybox: MediaSourceType
MediaSourceType_RecentsFavorites: MediaSourceType
MediaSourceType_HomeApps: MediaSourceType
MediaSourceType_Search: MediaSourceType

class VehicleData(_message.Message):
    __slots__ = (
        "charge_schedule_state",
        "charge_state",
        "climate_state",
        "closures_state",
        "drive_state",
        "location_state",
        "media_detail_state",
        "media_state",
        "parental_controls_state",
        "preconditioning_schedule_state",
        "software_update_state",
        "tire_pressure_state",
    )
    CHARGE_STATE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_STATE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_STATE_FIELD_NUMBER: _ClassVar[int]
    CLOSURES_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULE_STATE_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_SCHEDULE_STATE_FIELD_NUMBER: _ClassVar[int]
    TIRE_PRESSURE_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DETAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_STATE_FIELD_NUMBER: _ClassVar[int]
    charge_state: ChargeState
    climate_state: ClimateState
    drive_state: DriveState
    location_state: LocationState
    closures_state: ClosuresState
    charge_schedule_state: ChargeScheduleState
    preconditioning_schedule_state: PreconditioningScheduleState
    tire_pressure_state: TirePressureState
    media_state: MediaState
    media_detail_state: MediaDetailState
    software_update_state: SoftwareUpdateState
    parental_controls_state: ParentalControlsState

    def __init__(
        self,
        charge_state: ChargeState | _Mapping | None = ...,
        climate_state: ClimateState | _Mapping | None = ...,
        drive_state: DriveState | _Mapping | None = ...,
        location_state: LocationState | _Mapping | None = ...,
        closures_state: ClosuresState | _Mapping | None = ...,
        charge_schedule_state: ChargeScheduleState | _Mapping | None = ...,
        preconditioning_schedule_state: PreconditioningScheduleState
        | _Mapping
        | None = ...,
        tire_pressure_state: TirePressureState | _Mapping | None = ...,
        media_state: MediaState | _Mapping | None = ...,
        media_detail_state: MediaDetailState | _Mapping | None = ...,
        software_update_state: SoftwareUpdateState | _Mapping | None = ...,
        parental_controls_state: ParentalControlsState | _Mapping | None = ...,
    ) -> None: ...

class ClosuresState(_message.Message):
    __slots__ = (
        "center_display_state",
        "door_open_driver_front",
        "door_open_driver_rear",
        "door_open_passenger_front",
        "door_open_passenger_rear",
        "door_open_trunk_front",
        "door_open_trunk_rear",
        "is_user_present",
        "locked",
        "remote_start",
        "sentry_mode_available",
        "sentry_mode_state",
        "speed_limit_mode",
        "sun_roof_percent_open",
        "sun_roof_state",
        "timestamp",
        "tonneau_in_motion",
        "tonneau_percent_open",
        "tonneau_state",
        "valet_mode",
        "valet_pin_needed",
        "window_open_driver_front",
        "window_open_driver_rear",
        "window_open_passenger_front",
        "window_open_passenger_rear",
    )

    class SunRoofState(_message.Message):
        __slots__ = ("Calibrating", "Closed", "Moving", "Open", "Unknown", "Vent")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        CALIBRATING_FIELD_NUMBER: _ClassVar[int]
        CLOSED_FIELD_NUMBER: _ClassVar[int]
        OPEN_FIELD_NUMBER: _ClassVar[int]
        MOVING_FIELD_NUMBER: _ClassVar[int]
        VENT_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Calibrating: _common_pb2.Void
        Closed: _common_pb2.Void
        Open: _common_pb2.Void
        Moving: _common_pb2.Void
        Vent: _common_pb2.Void

        def __init__(
            self,
            Unknown: _common_pb2.Void | _Mapping | None = ...,
            Calibrating: _common_pb2.Void | _Mapping | None = ...,
            Closed: _common_pb2.Void | _Mapping | None = ...,
            Open: _common_pb2.Void | _Mapping | None = ...,
            Moving: _common_pb2.Void | _Mapping | None = ...,
            Vent: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class DisplayState(_message.Message):
        __slots__ = (
            "Accessory",
            "Charging",
            "Dim",
            "Dog",
            "Driving",
            "Entertainment",
            "Lock",
            "Off",
            "On",
            "Sentry",
        )
        OFF_FIELD_NUMBER: _ClassVar[int]
        DIM_FIELD_NUMBER: _ClassVar[int]
        ACCESSORY_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        DRIVING_FIELD_NUMBER: _ClassVar[int]
        CHARGING_FIELD_NUMBER: _ClassVar[int]
        LOCK_FIELD_NUMBER: _ClassVar[int]
        SENTRY_FIELD_NUMBER: _ClassVar[int]
        DOG_FIELD_NUMBER: _ClassVar[int]
        ENTERTAINMENT_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Dim: _common_pb2.Void
        Accessory: _common_pb2.Void
        On: _common_pb2.Void
        Driving: _common_pb2.Void
        Charging: _common_pb2.Void
        Lock: _common_pb2.Void
        Sentry: _common_pb2.Void
        Dog: _common_pb2.Void
        Entertainment: _common_pb2.Void

        def __init__(
            self,
            Off: _common_pb2.Void | _Mapping | None = ...,
            Dim: _common_pb2.Void | _Mapping | None = ...,
            Accessory: _common_pb2.Void | _Mapping | None = ...,
            On: _common_pb2.Void | _Mapping | None = ...,
            Driving: _common_pb2.Void | _Mapping | None = ...,
            Charging: _common_pb2.Void | _Mapping | None = ...,
            Lock: _common_pb2.Void | _Mapping | None = ...,
            Sentry: _common_pb2.Void | _Mapping | None = ...,
            Dog: _common_pb2.Void | _Mapping | None = ...,
            Entertainment: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class SentryModeState(_message.Message):
        __slots__ = ("Armed", "Aware", "Idle", "Off", "Panic", "Quiet")
        OFF_FIELD_NUMBER: _ClassVar[int]
        IDLE_FIELD_NUMBER: _ClassVar[int]
        ARMED_FIELD_NUMBER: _ClassVar[int]
        AWARE_FIELD_NUMBER: _ClassVar[int]
        PANIC_FIELD_NUMBER: _ClassVar[int]
        QUIET_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Idle: _common_pb2.Void
        Armed: _common_pb2.Void
        Aware: _common_pb2.Void
        Panic: _common_pb2.Void
        Quiet: _common_pb2.Void

        def __init__(
            self,
            Off: _common_pb2.Void | _Mapping | None = ...,
            Idle: _common_pb2.Void | _Mapping | None = ...,
            Armed: _common_pb2.Void | _Mapping | None = ...,
            Aware: _common_pb2.Void | _Mapping | None = ...,
            Panic: _common_pb2.Void | _Mapping | None = ...,
            Quiet: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    DOOR_OPEN_DRIVER_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_DRIVER_REAR_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_PASSENGER_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_PASSENGER_REAR_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_TRUNK_FRONT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_TRUNK_REAR_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_DRIVER_FRONT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_PASSENGER_FRONT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_DRIVER_REAR_FIELD_NUMBER: _ClassVar[int]
    WINDOW_OPEN_PASSENGER_REAR_FIELD_NUMBER: _ClassVar[int]
    SUN_ROOF_STATE_FIELD_NUMBER: _ClassVar[int]
    SUN_ROOF_PERCENT_OPEN_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_USER_PRESENT_FIELD_NUMBER: _ClassVar[int]
    CENTER_DISPLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_START_FIELD_NUMBER: _ClassVar[int]
    VALET_MODE_FIELD_NUMBER: _ClassVar[int]
    VALET_PIN_NEEDED_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_STATE_FIELD_NUMBER: _ClassVar[int]
    SENTRY_MODE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SPEED_LIMIT_MODE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_STATE_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_PERCENT_OPEN_FIELD_NUMBER: _ClassVar[int]
    TONNEAU_IN_MOTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    door_open_driver_front: bool
    door_open_driver_rear: bool
    door_open_passenger_front: bool
    door_open_passenger_rear: bool
    door_open_trunk_front: bool
    door_open_trunk_rear: bool
    window_open_driver_front: bool
    window_open_passenger_front: bool
    window_open_driver_rear: bool
    window_open_passenger_rear: bool
    sun_roof_state: ClosuresState.SunRoofState
    sun_roof_percent_open: int
    locked: bool
    is_user_present: bool
    center_display_state: ClosuresState.DisplayState
    remote_start: bool
    valet_mode: bool
    valet_pin_needed: bool
    sentry_mode_state: ClosuresState.SentryModeState
    sentry_mode_available: bool
    speed_limit_mode: SpeedLimitMode
    tonneau_state: _vcsec_pb2.ClosureState_E
    tonneau_percent_open: int
    tonneau_in_motion: bool
    timestamp: _timestamp_pb2.Timestamp

    def __init__(
        self,
        door_open_driver_front: bool = ...,
        door_open_driver_rear: bool = ...,
        door_open_passenger_front: bool = ...,
        door_open_passenger_rear: bool = ...,
        door_open_trunk_front: bool = ...,
        door_open_trunk_rear: bool = ...,
        window_open_driver_front: bool = ...,
        window_open_passenger_front: bool = ...,
        window_open_driver_rear: bool = ...,
        window_open_passenger_rear: bool = ...,
        sun_roof_state: ClosuresState.SunRoofState | _Mapping | None = ...,
        sun_roof_percent_open: int | None = ...,
        locked: bool = ...,
        is_user_present: bool = ...,
        center_display_state: ClosuresState.DisplayState | _Mapping | None = ...,
        remote_start: bool = ...,
        valet_mode: bool = ...,
        valet_pin_needed: bool = ...,
        sentry_mode_state: ClosuresState.SentryModeState | _Mapping | None = ...,
        sentry_mode_available: bool = ...,
        speed_limit_mode: SpeedLimitMode | _Mapping | None = ...,
        tonneau_state: _vcsec_pb2.ClosureState_E | str | None = ...,
        tonneau_percent_open: int | None = ...,
        tonneau_in_motion: bool = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class ChargeScheduleState(_message.Message):
    __slots__ = (
        "charge_buffer",
        "charge_schedule_window",
        "charge_schedules",
        "max_num_charge_schedules",
        "next_schedule",
        "show_schedule_complete_state",
        "timestamp",
    )
    CHARGE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    CHARGE_SCHEDULE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CHARGE_BUFFER_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_CHARGE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SHOW_SCHEDULE_COMPLETE_STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    charge_schedules: _containers.RepeatedCompositeFieldContainer[
        _common_pb2.ChargeSchedule
    ]
    charge_schedule_window: _common_pb2.ChargeSchedule
    charge_buffer: int
    max_num_charge_schedules: int
    next_schedule: bool
    show_schedule_complete_state: bool
    timestamp: _timestamp_pb2.Timestamp

    def __init__(
        self,
        charge_schedules: _Iterable[_common_pb2.ChargeSchedule | _Mapping] | None = ...,
        charge_schedule_window: _common_pb2.ChargeSchedule | _Mapping | None = ...,
        charge_buffer: int | None = ...,
        max_num_charge_schedules: int | None = ...,
        next_schedule: bool = ...,
        show_schedule_complete_state: bool = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class PreconditioningScheduleState(_message.Message):
    __slots__ = (
        "max_num_precondition_schedules",
        "next_schedule",
        "precondition_schedules",
        "preconditioning_schedule_window",
        "timestamp",
    )
    PRECONDITION_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_SCHEDULE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_PRECONDITION_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    precondition_schedules: _containers.RepeatedCompositeFieldContainer[
        _common_pb2.PreconditionSchedule
    ]
    preconditioning_schedule_window: _common_pb2.PreconditionSchedule
    max_num_precondition_schedules: int
    next_schedule: bool
    timestamp: _timestamp_pb2.Timestamp

    def __init__(
        self,
        precondition_schedules: _Iterable[_common_pb2.PreconditionSchedule | _Mapping]
        | None = ...,
        preconditioning_schedule_window: _common_pb2.PreconditionSchedule
        | _Mapping
        | None = ...,
        max_num_precondition_schedules: int | None = ...,
        next_schedule: bool = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class SpeedLimitMode(_message.Message):
    __slots__ = (
        "active",
        "current_limit_mph",
        "max_limit_mph",
        "min_limit_mph",
        "pin_code_set",
    )
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PIN_CODE_SET_FIELD_NUMBER: _ClassVar[int]
    MAX_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    MIN_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    active: bool
    pin_code_set: bool
    max_limit_mph: float
    min_limit_mph: float
    current_limit_mph: float

    def __init__(
        self,
        active: bool = ...,
        pin_code_set: bool = ...,
        max_limit_mph: float | None = ...,
        min_limit_mph: float | None = ...,
        current_limit_mph: float | None = ...,
    ) -> None: ...

class ParentalControlsSettings(_message.Message):
    __slots__ = (
        "chill_acceleration_enabled",
        "curfew_enabled",
        "curfew_end_time",
        "curfew_start_time",
        "current_limit_mph",
        "max_limit_mph",
        "min_limit_mph",
        "require_safety_settings_enabled",
        "speed_limit_enabled",
    )
    SPEED_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    MIN_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    CHILL_ACCELERATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SAFETY_SETTINGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURFEW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURFEW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CURFEW_END_TIME_FIELD_NUMBER: _ClassVar[int]
    speed_limit_enabled: bool
    max_limit_mph: float
    min_limit_mph: float
    current_limit_mph: float
    chill_acceleration_enabled: bool
    require_safety_settings_enabled: bool
    curfew_enabled: bool
    curfew_start_time: int
    curfew_end_time: int

    def __init__(
        self,
        speed_limit_enabled: bool = ...,
        max_limit_mph: float | None = ...,
        min_limit_mph: float | None = ...,
        current_limit_mph: float | None = ...,
        chill_acceleration_enabled: bool = ...,
        require_safety_settings_enabled: bool = ...,
        curfew_enabled: bool = ...,
        curfew_start_time: int | None = ...,
        curfew_end_time: int | None = ...,
    ) -> None: ...

class ParentalControlsState(_message.Message):
    __slots__ = (
        "parental_controls_active",
        "parental_controls_pin_set",
        "parental_controls_settings",
        "timestamp",
    )
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_PIN_SET_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_CONTROLS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    parental_controls_active: bool
    parental_controls_pin_set: bool
    parental_controls_settings: ParentalControlsSettings

    def __init__(
        self,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        parental_controls_active: bool = ...,
        parental_controls_pin_set: bool = ...,
        parental_controls_settings: ParentalControlsSettings | _Mapping | None = ...,
    ) -> None: ...

class SoftwareUpdateState(_message.Message):
    __slots__ = (
        "download_perc",
        "expected_duration_sec",
        "install_perc",
        "scheduled_time_ms",
        "status",
        "timestamp",
        "version",
        "warning_time_remaining_ms",
    )

    class SoftwareUpdateStatus(_message.Message):
        __slots__ = (
            "Available",
            "Downloading",
            "DownloadingWifiWait",
            "Installing",
            "Scheduled",
            "Unknown",
        )
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        INSTALLING_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADINGWIFIWAIT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Installing: _common_pb2.Void
        Scheduled: _common_pb2.Void
        Available: _common_pb2.Void
        DownloadingWifiWait: _common_pb2.Void
        Downloading: _common_pb2.Void

        def __init__(
            self,
            Unknown: _common_pb2.Void | _Mapping | None = ...,
            Installing: _common_pb2.Void | _Mapping | None = ...,
            Scheduled: _common_pb2.Void | _Mapping | None = ...,
            Available: _common_pb2.Void | _Mapping | None = ...,
            DownloadingWifiWait: _common_pb2.Void | _Mapping | None = ...,
            Downloading: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WARNING_TIME_REMAINING_MS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PERC_FIELD_NUMBER: _ClassVar[int]
    INSTALL_PERC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: SoftwareUpdateState.SoftwareUpdateStatus
    scheduled_time_ms: int
    warning_time_remaining_ms: int
    expected_duration_sec: int
    download_perc: int
    install_perc: int
    version: str
    timestamp: _timestamp_pb2.Timestamp

    def __init__(
        self,
        status: SoftwareUpdateState.SoftwareUpdateStatus | _Mapping | None = ...,
        scheduled_time_ms: int | None = ...,
        warning_time_remaining_ms: int | None = ...,
        expected_duration_sec: int | None = ...,
        download_perc: int | None = ...,
        install_perc: int | None = ...,
        version: str | None = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class DriveState(_message.Message):
    __slots__ = (
        "active_route_coordinates",
        "active_route_destination",
        "active_route_energy_at_arrival",
        "active_route_miles_to_arrival",
        "active_route_minutes_to_arrival",
        "active_route_traffic_minutes_delay",
        "last_route_update",
        "last_traffic_update",
        "odometer_in_hundredths_of_a_mile",
        "power",
        "shift_state",
        "speed",
        "speed_float",
        "timestamp",
    )
    SHIFT_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ODOMETER_IN_HUNDREDTHS_OF_A_MILE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_MINUTES_TO_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_MILES_TO_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_TRAFFIC_MINUTES_DELAY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_ENERGY_AT_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    LAST_ROUTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRAFFIC_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ROUTE_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    shift_state: ShiftState
    speed: int
    power: int
    timestamp: _timestamp_pb2.Timestamp
    odometer_in_hundredths_of_a_mile: int
    speed_float: float
    active_route_destination: str
    active_route_minutes_to_arrival: float
    active_route_miles_to_arrival: float
    active_route_traffic_minutes_delay: float
    active_route_energy_at_arrival: float
    last_route_update: int
    last_traffic_update: _timestamp_pb2.Timestamp
    active_route_coordinates: _common_pb2.LatLong

    def __init__(
        self,
        shift_state: ShiftState | _Mapping | None = ...,
        speed: int | None = ...,
        power: int | None = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        odometer_in_hundredths_of_a_mile: int | None = ...,
        speed_float: float | None = ...,
        active_route_destination: str | None = ...,
        active_route_minutes_to_arrival: float | None = ...,
        active_route_miles_to_arrival: float | None = ...,
        active_route_traffic_minutes_delay: float | None = ...,
        active_route_energy_at_arrival: float | None = ...,
        last_route_update: int | None = ...,
        last_traffic_update: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        active_route_coordinates: _common_pb2.LatLong | _Mapping | None = ...,
    ) -> None: ...

class ChargeState(_message.Message):
    __slots__ = (
        "battery_level",
        "battery_range",
        "charge_cable_unlatched",
        "charge_current_request",
        "charge_current_request_max",
        "charge_enable_request",
        "charge_energy_added",
        "charge_limit_reason",
        "charge_limit_soc",
        "charge_limit_soc_max",
        "charge_limit_soc_min",
        "charge_limit_soc_std",
        "charge_miles_added_ideal",
        "charge_miles_added_rated",
        "charge_port_cold_weather_mode",
        "charge_port_color",
        "charge_port_door_open",
        "charge_port_latch",
        "charge_rate_mph",
        "charge_rate_mph_float",
        "charger_actual_current",
        "charger_phases",
        "charger_pilot_current",
        "charger_power",
        "charger_voltage",
        "charging_amps",
        "charging_state",
        "conn_charge_cable",
        "est_battery_range",
        "fast_charger_brand",
        "fast_charger_present",
        "fast_charger_type",
        "home_location",
        "ideal_battery_range",
        "managed_charging_active",
        "managed_charging_start_time",
        "managed_charging_state",
        "managed_charging_user_canceled",
        "max_range_charge_counter",
        "minutes_to_charge_limit",
        "minutes_to_full_charge",
        "off_peak_charging_times",
        "off_peak_hours_end_time",
        "one_time_soc_limit",
        "outlet_max_timer_minutes",
        "outlet_soc_limit",
        "outlet_state",
        "outlet_time_remaining",
        "power_feed_soc_limit",
        "power_feed_state",
        "power_feed_time_remaining",
        "powershare_feature_allowed",
        "powershare_feature_enabled",
        "powershare_instantaneous_load_kw",
        "powershare_request",
        "powershare_soc_limit",
        "powershare_status",
        "powershare_stop_reason",
        "powershare_type",
        "powershare_vehicle_energy_left_hr",
        "preconditioning_enabled",
        "preconditioning_times",
        "scheduled_charging_mode",
        "scheduled_charging_pending",
        "scheduled_charging_start_time",
        "scheduled_charging_start_time_app",
        "scheduled_charging_start_time_minutes",
        "scheduled_departure_time",
        "scheduled_departure_time_minutes",
        "supercharger_session_trip_planner",
        "timestamp",
        "trip_charging",
        "usable_battery_level",
        "user_charge_enable_request",
        "work_location",
    )

    class ScheduledChargingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ScheduledChargingModeOff: _ClassVar[ChargeState.ScheduledChargingMode]
        ScheduledChargingModeStartAt: _ClassVar[ChargeState.ScheduledChargingMode]
        ScheduledChargingModeDepartBy: _ClassVar[ChargeState.ScheduledChargingMode]

    ScheduledChargingModeOff: ChargeState.ScheduledChargingMode
    ScheduledChargingModeStartAt: ChargeState.ScheduledChargingMode
    ScheduledChargingModeDepartBy: ChargeState.ScheduledChargingMode

    class ChargePortColor_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ChargePortColorOff: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorRed: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorGreen: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorBlue: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorWhite: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingGreen: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingAmber: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorAmber: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorRave: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorDebug: _ClassVar[ChargeState.ChargePortColor_E]
        ChargePortColorFlashingBlue: _ClassVar[ChargeState.ChargePortColor_E]

    ChargePortColorOff: ChargeState.ChargePortColor_E
    ChargePortColorRed: ChargeState.ChargePortColor_E
    ChargePortColorGreen: ChargeState.ChargePortColor_E
    ChargePortColorBlue: ChargeState.ChargePortColor_E
    ChargePortColorWhite: ChargeState.ChargePortColor_E
    ChargePortColorFlashingGreen: ChargeState.ChargePortColor_E
    ChargePortColorFlashingAmber: ChargeState.ChargePortColor_E
    ChargePortColorAmber: ChargeState.ChargePortColor_E
    ChargePortColorRave: ChargeState.ChargePortColor_E
    ChargePortColorDebug: ChargeState.ChargePortColor_E
    ChargePortColorFlashingBlue: ChargeState.ChargePortColor_E

    class ChargeLimitReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ChargeLimitReasonUnknown: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonNone: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonEvse: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonBattTempLow: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonHighSoc: _ClassVar[ChargeState.ChargeLimitReason]
        ChargeLimitReasonCabin: _ClassVar[ChargeState.ChargeLimitReason]

    ChargeLimitReasonUnknown: ChargeState.ChargeLimitReason
    ChargeLimitReasonNone: ChargeState.ChargeLimitReason
    ChargeLimitReasonEvse: ChargeState.ChargeLimitReason
    ChargeLimitReasonBattTempLow: ChargeState.ChargeLimitReason
    ChargeLimitReasonHighSoc: ChargeState.ChargeLimitReason
    ChargeLimitReasonCabin: ChargeState.ChargeLimitReason

    class OutletState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OutletStateOff: _ClassVar[ChargeState.OutletState]
        OutletStateCabinAndBed: _ClassVar[ChargeState.OutletState]
        OutletStateCabin: _ClassVar[ChargeState.OutletState]

    OutletStateOff: ChargeState.OutletState
    OutletStateCabinAndBed: ChargeState.OutletState
    OutletStateCabin: ChargeState.OutletState

    class PowerFeedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowerFeedStateOff: _ClassVar[ChargeState.PowerFeedState]
        PowerFeedStateCabinAndBed: _ClassVar[ChargeState.PowerFeedState]
        PowerFeedStateCabin: _ClassVar[ChargeState.PowerFeedState]

    PowerFeedStateOff: ChargeState.PowerFeedState
    PowerFeedStateCabinAndBed: ChargeState.PowerFeedState
    PowerFeedStateCabin: ChargeState.PowerFeedState

    class PowershareStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareStatusInactive: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusInit: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusActive: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusStopped: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusHandshaking: _ClassVar[ChargeState.PowershareStatus]
        PowershareStatusActiveReconnectingSoon: _ClassVar[ChargeState.PowershareStatus]

    PowershareStatusInactive: ChargeState.PowershareStatus
    PowershareStatusInit: ChargeState.PowershareStatus
    PowershareStatusActive: ChargeState.PowershareStatus
    PowershareStatusStopped: ChargeState.PowershareStatus
    PowershareStatusHandshaking: ChargeState.PowershareStatus
    PowershareStatusActiveReconnectingSoon: ChargeState.PowershareStatus

    class PowershareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareTypeNone: _ClassVar[ChargeState.PowershareType]
        PowershareTypeLoad: _ClassVar[ChargeState.PowershareType]
        PowershareTypeHome: _ClassVar[ChargeState.PowershareType]

    PowershareTypeNone: ChargeState.PowershareType
    PowershareTypeLoad: ChargeState.PowershareType
    PowershareTypeHome: ChargeState.PowershareType

    class PowershareStopReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PowershareStopReasonNone: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonSOCTooLow: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonRetry: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonFault: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonUser: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonReconnecting: _ClassVar[ChargeState.PowershareStopReason]
        PowershareStopReasonAuthentication: _ClassVar[ChargeState.PowershareStopReason]

    PowershareStopReasonNone: ChargeState.PowershareStopReason
    PowershareStopReasonSOCTooLow: ChargeState.PowershareStopReason
    PowershareStopReasonRetry: ChargeState.PowershareStopReason
    PowershareStopReasonFault: ChargeState.PowershareStopReason
    PowershareStopReasonUser: ChargeState.PowershareStopReason
    PowershareStopReasonReconnecting: ChargeState.PowershareStopReason
    PowershareStopReasonAuthentication: ChargeState.PowershareStopReason

    class CableType(_message.Message):
        __slots__ = ("GB_AC", "GB_DC", "IEC", "SAE", "SNA")
        SNA_FIELD_NUMBER: _ClassVar[int]
        IEC_FIELD_NUMBER: _ClassVar[int]
        SAE_FIELD_NUMBER: _ClassVar[int]
        GB_AC_FIELD_NUMBER: _ClassVar[int]
        GB_DC_FIELD_NUMBER: _ClassVar[int]
        SNA: _common_pb2.Void
        IEC: _common_pb2.Void
        SAE: _common_pb2.Void
        GB_AC: _common_pb2.Void
        GB_DC: _common_pb2.Void

        def __init__(
            self,
            SNA: _common_pb2.Void | _Mapping | None = ...,
            IEC: _common_pb2.Void | _Mapping | None = ...,
            SAE: _common_pb2.Void | _Mapping | None = ...,
            GB_AC: _common_pb2.Void | _Mapping | None = ...,
            GB_DC: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class ChargerType(_message.Message):
        __slots__ = (
            "ACSingleWireCAN",
            "Chademo",
            "Combo",
            "Gb",
            "MCSingleWireCAN",
            "Other",
            "SNA",
            "Supercharger",
            "Tesla",
        )
        SNA_FIELD_NUMBER: _ClassVar[int]
        SUPERCHARGER_FIELD_NUMBER: _ClassVar[int]
        CHADEMO_FIELD_NUMBER: _ClassVar[int]
        GB_FIELD_NUMBER: _ClassVar[int]
        ACSINGLEWIRECAN_FIELD_NUMBER: _ClassVar[int]
        COMBO_FIELD_NUMBER: _ClassVar[int]
        MCSINGLEWIRECAN_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_NUMBER: _ClassVar[int]
        TESLA_FIELD_NUMBER: _ClassVar[int]
        SNA: _common_pb2.Void
        Supercharger: _common_pb2.Void
        Chademo: _common_pb2.Void
        Gb: _common_pb2.Void
        ACSingleWireCAN: _common_pb2.Void
        Combo: _common_pb2.Void
        MCSingleWireCAN: _common_pb2.Void
        Other: _common_pb2.Void
        Tesla: _common_pb2.Void

        def __init__(
            self,
            SNA: _common_pb2.Void | _Mapping | None = ...,
            Supercharger: _common_pb2.Void | _Mapping | None = ...,
            Chademo: _common_pb2.Void | _Mapping | None = ...,
            Gb: _common_pb2.Void | _Mapping | None = ...,
            ACSingleWireCAN: _common_pb2.Void | _Mapping | None = ...,
            Combo: _common_pb2.Void | _Mapping | None = ...,
            MCSingleWireCAN: _common_pb2.Void | _Mapping | None = ...,
            Other: _common_pb2.Void | _Mapping | None = ...,
            Tesla: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class ChargingState(_message.Message):
        __slots__ = (
            "Calibrating",
            "Charging",
            "Complete",
            "Disconnected",
            "NoPower",
            "Starting",
            "Stopped",
            "Unknown",
        )
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        NOPOWER_FIELD_NUMBER: _ClassVar[int]
        STARTING_FIELD_NUMBER: _ClassVar[int]
        CHARGING_FIELD_NUMBER: _ClassVar[int]
        COMPLETE_FIELD_NUMBER: _ClassVar[int]
        STOPPED_FIELD_NUMBER: _ClassVar[int]
        CALIBRATING_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Disconnected: _common_pb2.Void
        NoPower: _common_pb2.Void
        Starting: _common_pb2.Void
        Charging: _common_pb2.Void
        Complete: _common_pb2.Void
        Stopped: _common_pb2.Void
        Calibrating: _common_pb2.Void

        def __init__(
            self,
            Unknown: _common_pb2.Void | _Mapping | None = ...,
            Disconnected: _common_pb2.Void | _Mapping | None = ...,
            NoPower: _common_pb2.Void | _Mapping | None = ...,
            Starting: _common_pb2.Void | _Mapping | None = ...,
            Charging: _common_pb2.Void | _Mapping | None = ...,
            Complete: _common_pb2.Void | _Mapping | None = ...,
            Stopped: _common_pb2.Void | _Mapping | None = ...,
            Calibrating: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class ChargerBrand(_message.Message):
        __slots__ = ("SNA", "Tesla")
        TESLA_FIELD_NUMBER: _ClassVar[int]
        SNA_FIELD_NUMBER: _ClassVar[int]
        Tesla: _common_pb2.Void
        SNA: _common_pb2.Void

        def __init__(
            self,
            Tesla: _common_pb2.Void | _Mapping | None = ...,
            SNA: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    CHARGING_STATE_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_BRAND_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_STD_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_MIN_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_SOC_MAX_FIELD_NUMBER: _ClassVar[int]
    MAX_RANGE_CHARGE_COUNTER_FIELD_NUMBER: _ClassVar[int]
    FAST_CHARGER_PRESENT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    EST_BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    IDEAL_BATTERY_RANGE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USABLE_BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ENERGY_ADDED_FIELD_NUMBER: _ClassVar[int]
    CHARGE_MILES_ADDED_RATED_FIELD_NUMBER: _ClassVar[int]
    CHARGE_MILES_ADDED_IDEAL_FIELD_NUMBER: _ClassVar[int]
    CHARGER_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CHARGER_PILOT_CURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGER_ACTUAL_CURRENT_FIELD_NUMBER: _ClassVar[int]
    CHARGER_POWER_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_FULL_CHARGE_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_CHARGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRIP_CHARGING_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MPH_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_DOOR_OPEN_FIELD_NUMBER: _ClassVar[int]
    CONN_CHARGE_CABLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_PENDING_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_CHARGE_ENABLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ENABLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGER_PHASES_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_LATCH_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_COLD_WEATHER_MODE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CURRENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CURRENT_REQUEST_MAX_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_USER_CANCELED_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_CHARGING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_HOURS_END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_MODE_FIELD_NUMBER: _ClassVar[int]
    CHARGING_AMPS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DEPARTURE_TIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CHARGING_START_TIME_APP_FIELD_NUMBER: _ClassVar[int]
    SUPERCHARGER_SESSION_TRIP_PLANNER_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PORT_COLOR_FIELD_NUMBER: _ClassVar[int]
    CHARGE_RATE_MPH_FLOAT_FIELD_NUMBER: _ClassVar[int]
    CHARGE_LIMIT_REASON_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CHARGING_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_CABLE_UNLATCHED_FIELD_NUMBER: _ClassVar[int]
    OUTLET_STATE_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_STATE_FIELD_NUMBER: _ClassVar[int]
    OUTLET_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OUTLET_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_FEATURE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STATUS_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_INSTANTANEOUS_LOAD_KW_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_VEHICLE_ENERGY_LEFT_HR_FIELD_NUMBER: _ClassVar[int]
    POWERSHARE_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_SOC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HOME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WORK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OUTLET_MAX_TIMER_MINUTES_FIELD_NUMBER: _ClassVar[int]
    charging_state: ChargeState.ChargingState
    fast_charger_type: ChargeState.ChargerType
    fast_charger_brand: ChargeState.ChargerBrand
    charge_limit_soc: int
    charge_limit_soc_std: int
    charge_limit_soc_min: int
    charge_limit_soc_max: int
    max_range_charge_counter: int
    fast_charger_present: bool
    battery_range: float
    est_battery_range: float
    ideal_battery_range: float
    battery_level: int
    usable_battery_level: int
    charge_energy_added: float
    charge_miles_added_rated: float
    charge_miles_added_ideal: float
    charger_voltage: int
    charger_pilot_current: int
    charger_actual_current: int
    charger_power: int
    minutes_to_full_charge: int
    minutes_to_charge_limit: int
    trip_charging: bool
    charge_rate_mph: int
    charge_port_door_open: bool
    conn_charge_cable: ChargeState.CableType
    scheduled_charging_start_time: int
    scheduled_charging_pending: bool
    scheduled_departure_time: _timestamp_pb2.Timestamp
    user_charge_enable_request: bool
    charge_enable_request: bool
    charger_phases: int
    charge_port_latch: _common_pb2.ChargePortLatchState
    charge_port_cold_weather_mode: bool
    charge_current_request: int
    charge_current_request_max: int
    managed_charging_active: bool
    managed_charging_user_canceled: bool
    managed_charging_start_time: int
    timestamp: _timestamp_pb2.Timestamp
    preconditioning_times: _common_pb2.PreconditioningTimes
    off_peak_charging_times: _common_pb2.OffPeakChargingTimes
    off_peak_hours_end_time: int
    scheduled_charging_mode: ChargeState.ScheduledChargingMode
    charging_amps: int
    scheduled_charging_start_time_minutes: int
    scheduled_departure_time_minutes: int
    preconditioning_enabled: bool
    scheduled_charging_start_time_app: int
    supercharger_session_trip_planner: bool
    charge_port_color: ChargeState.ChargePortColor_E
    charge_rate_mph_float: float
    charge_limit_reason: ChargeState.ChargeLimitReason
    managed_charging_state: ManagedChargingState
    charge_cable_unlatched: bool
    outlet_state: ChargeState.OutletState
    power_feed_state: ChargeState.PowerFeedState
    outlet_soc_limit: int
    power_feed_soc_limit: int
    outlet_time_remaining: int
    power_feed_time_remaining: int
    powershare_feature_allowed: bool
    powershare_feature_enabled: bool
    powershare_request: bool
    powershare_type: ChargeState.PowershareType
    powershare_status: ChargeState.PowershareStatus
    powershare_stop_reason: ChargeState.PowershareStopReason
    powershare_instantaneous_load_kw: float
    powershare_vehicle_energy_left_hr: int
    powershare_soc_limit: int
    one_time_soc_limit: int
    home_location: _common_pb2.LatLong
    work_location: _common_pb2.LatLong
    outlet_max_timer_minutes: int

    def __init__(
        self,
        charging_state: ChargeState.ChargingState | _Mapping | None = ...,
        fast_charger_type: ChargeState.ChargerType | _Mapping | None = ...,
        fast_charger_brand: ChargeState.ChargerBrand | _Mapping | None = ...,
        charge_limit_soc: int | None = ...,
        charge_limit_soc_std: int | None = ...,
        charge_limit_soc_min: int | None = ...,
        charge_limit_soc_max: int | None = ...,
        max_range_charge_counter: int | None = ...,
        fast_charger_present: bool = ...,
        battery_range: float | None = ...,
        est_battery_range: float | None = ...,
        ideal_battery_range: float | None = ...,
        battery_level: int | None = ...,
        usable_battery_level: int | None = ...,
        charge_energy_added: float | None = ...,
        charge_miles_added_rated: float | None = ...,
        charge_miles_added_ideal: float | None = ...,
        charger_voltage: int | None = ...,
        charger_pilot_current: int | None = ...,
        charger_actual_current: int | None = ...,
        charger_power: int | None = ...,
        minutes_to_full_charge: int | None = ...,
        minutes_to_charge_limit: int | None = ...,
        trip_charging: bool = ...,
        charge_rate_mph: int | None = ...,
        charge_port_door_open: bool = ...,
        conn_charge_cable: ChargeState.CableType | _Mapping | None = ...,
        scheduled_charging_start_time: int | None = ...,
        scheduled_charging_pending: bool = ...,
        scheduled_departure_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        user_charge_enable_request: bool = ...,
        charge_enable_request: bool = ...,
        charger_phases: int | None = ...,
        charge_port_latch: _common_pb2.ChargePortLatchState | _Mapping | None = ...,
        charge_port_cold_weather_mode: bool = ...,
        charge_current_request: int | None = ...,
        charge_current_request_max: int | None = ...,
        managed_charging_active: bool = ...,
        managed_charging_user_canceled: bool = ...,
        managed_charging_start_time: int | None = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        preconditioning_times: _common_pb2.PreconditioningTimes | _Mapping | None = ...,
        off_peak_charging_times: _common_pb2.OffPeakChargingTimes
        | _Mapping
        | None = ...,
        off_peak_hours_end_time: int | None = ...,
        scheduled_charging_mode: ChargeState.ScheduledChargingMode | str | None = ...,
        charging_amps: int | None = ...,
        scheduled_charging_start_time_minutes: int | None = ...,
        scheduled_departure_time_minutes: int | None = ...,
        preconditioning_enabled: bool = ...,
        scheduled_charging_start_time_app: int | None = ...,
        supercharger_session_trip_planner: bool = ...,
        charge_port_color: ChargeState.ChargePortColor_E | str | None = ...,
        charge_rate_mph_float: float | None = ...,
        charge_limit_reason: ChargeState.ChargeLimitReason | str | None = ...,
        managed_charging_state: ManagedChargingState | _Mapping | None = ...,
        charge_cable_unlatched: bool = ...,
        outlet_state: ChargeState.OutletState | str | None = ...,
        power_feed_state: ChargeState.PowerFeedState | str | None = ...,
        outlet_soc_limit: int | None = ...,
        power_feed_soc_limit: int | None = ...,
        outlet_time_remaining: int | None = ...,
        power_feed_time_remaining: int | None = ...,
        powershare_feature_allowed: bool = ...,
        powershare_feature_enabled: bool = ...,
        powershare_request: bool = ...,
        powershare_type: ChargeState.PowershareType | str | None = ...,
        powershare_status: ChargeState.PowershareStatus | str | None = ...,
        powershare_stop_reason: ChargeState.PowershareStopReason | str | None = ...,
        powershare_instantaneous_load_kw: float | None = ...,
        powershare_vehicle_energy_left_hr: int | None = ...,
        powershare_soc_limit: int | None = ...,
        one_time_soc_limit: int | None = ...,
        home_location: _common_pb2.LatLong | _Mapping | None = ...,
        work_location: _common_pb2.LatLong | _Mapping | None = ...,
        outlet_max_timer_minutes: int | None = ...,
    ) -> None: ...

class ManagedChargingState(_message.Message):
    __slots__ = (
        "charge_on_solar_gateway_din",
        "charge_on_solar_state",
        "minutes_to_lower_limit",
        "tesla_electric_asset_id",
    )
    CHARGE_ON_SOLAR_STATE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_ON_SOLAR_GATEWAY_DIN_FIELD_NUMBER: _ClassVar[int]
    TESLA_ELECTRIC_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    MINUTES_TO_LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    charge_on_solar_state: ChargeOnSolarState
    charge_on_solar_gateway_din: str
    tesla_electric_asset_id: str
    minutes_to_lower_limit: int

    def __init__(
        self,
        charge_on_solar_state: ChargeOnSolarState | _Mapping | None = ...,
        charge_on_solar_gateway_din: str | None = ...,
        tesla_electric_asset_id: str | None = ...,
        minutes_to_lower_limit: int | None = ...,
    ) -> None: ...

class ChargeOnSolarState(_message.Message):
    __slots__ = (
        "charging_on_anything",
        "charging_on_excess_solar",
        "error",
        "no_charge_recommended",
        "not_allowed",
        "user_disabled",
        "user_stopped",
        "waiting_for_server",
    )
    NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    NO_CHARGE_RECOMMENDED_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ON_EXCESS_SOLAR_FIELD_NUMBER: _ClassVar[int]
    CHARGING_ON_ANYTHING_FIELD_NUMBER: _ClassVar[int]
    USER_DISABLED_FIELD_NUMBER: _ClassVar[int]
    WAITING_FOR_SERVER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_STOPPED_FIELD_NUMBER: _ClassVar[int]
    not_allowed: ChargeOnSolarStateNotAllowed
    no_charge_recommended: ChargeOnSolarStateNoChargeRecommended
    charging_on_excess_solar: ChargeOnSolarStateChargingOnExcessSolar
    charging_on_anything: ChargeOnSolarStateChargingOnAnything
    user_disabled: ChargeOnSolarStateUserDisabled
    waiting_for_server: ChargeOnSolarStateWaitingForServer
    error: ChargeOnSolarStateError
    user_stopped: ChargeOnSolarStateUserStopped

    def __init__(
        self,
        not_allowed: ChargeOnSolarStateNotAllowed | _Mapping | None = ...,
        no_charge_recommended: ChargeOnSolarStateNoChargeRecommended
        | _Mapping
        | None = ...,
        charging_on_excess_solar: ChargeOnSolarStateChargingOnExcessSolar
        | _Mapping
        | None = ...,
        charging_on_anything: ChargeOnSolarStateChargingOnAnything
        | _Mapping
        | None = ...,
        user_disabled: ChargeOnSolarStateUserDisabled | _Mapping | None = ...,
        waiting_for_server: ChargeOnSolarStateWaitingForServer | _Mapping | None = ...,
        error: ChargeOnSolarStateError | _Mapping | None = ...,
        user_stopped: ChargeOnSolarStateUserStopped | _Mapping | None = ...,
    ) -> None: ...

class ChargeOnSolarStateNotAllowed(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateNoChargeRecommended(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _managed_charging_pb2.ChargeOnSolarNoChargeReason

    def __init__(
        self,
        reason: _managed_charging_pb2.ChargeOnSolarNoChargeReason | str | None = ...,
    ) -> None: ...

class ChargeOnSolarStateChargingOnExcessSolar(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateChargingOnAnything(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateUserDisabled(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateWaitingForServer(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateError(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargeOnSolarStateUserStopped(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class LocationState(_message.Message):
    __slots__ = (
        "corrected_latitude",
        "corrected_longitude",
        "estimated_gps_valid",
        "estimated_to_raw_distance",
        "geo_accuracy",
        "geo_elevation",
        "geo_heading",
        "geo_latitude",
        "geo_longitude",
        "gps_as_of",
        "heading",
        "homelink_nearby",
        "latitude",
        "location_name",
        "longitude",
        "native_latitude",
        "native_location_supported",
        "native_longitude",
        "native_type",
        "timestamp",
    )

    class GPSCoordinateType(_message.Message):
        __slots__ = ("GCJ", "WGS")
        GCJ_FIELD_NUMBER: _ClassVar[int]
        WGS_FIELD_NUMBER: _ClassVar[int]
        GCJ: _common_pb2.Void
        WGS: _common_pb2.Void

        def __init__(
            self,
            GCJ: _common_pb2.Void | _Mapping | None = ...,
            WGS: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    GPS_AS_OF_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LOCATION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HOMELINK_NEARBY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    GEO_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    GEO_HEADING_FIELD_NUMBER: _ClassVar[int]
    GEO_ELEVATION_FIELD_NUMBER: _ClassVar[int]
    GEO_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_GPS_VALID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TO_RAW_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    heading: int
    gps_as_of: int
    native_location_supported: bool
    native_latitude: float
    native_longitude: float
    native_type: LocationState.GPSCoordinateType
    corrected_latitude: float
    corrected_longitude: float
    timestamp: _timestamp_pb2.Timestamp
    homelink_nearby: bool
    location_name: str
    geo_latitude: float
    geo_longitude: float
    geo_heading: float
    geo_elevation: float
    geo_accuracy: float
    estimated_gps_valid: bool
    estimated_to_raw_distance: float

    def __init__(
        self,
        latitude: float | None = ...,
        longitude: float | None = ...,
        heading: int | None = ...,
        gps_as_of: int | None = ...,
        native_location_supported: bool = ...,
        native_latitude: float | None = ...,
        native_longitude: float | None = ...,
        native_type: LocationState.GPSCoordinateType | _Mapping | None = ...,
        corrected_latitude: float | None = ...,
        corrected_longitude: float | None = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        homelink_nearby: bool = ...,
        location_name: str | None = ...,
        geo_latitude: float | None = ...,
        geo_longitude: float | None = ...,
        geo_heading: float | None = ...,
        geo_elevation: float | None = ...,
        geo_accuracy: float | None = ...,
        estimated_gps_valid: bool = ...,
        estimated_to_raw_distance: float | None = ...,
    ) -> None: ...

class VehicleState(_message.Message):
    __slots__ = ("guestMode",)

    class GuestMode(_message.Message):
        __slots__ = ("GuestModeActive",)
        GUESTMODEACTIVE_FIELD_NUMBER: _ClassVar[int]
        GuestModeActive: bool

        def __init__(self, GuestModeActive: bool = ...) -> None: ...

    GUESTMODE_FIELD_NUMBER: _ClassVar[int]
    guestMode: VehicleState.GuestMode

    def __init__(
        self, guestMode: VehicleState.GuestMode | _Mapping | None = ...
    ) -> None: ...

class ClimateState(_message.Message):
    __slots__ = (
        "allow_cabin_overheat_protection",
        "auto_seat_climate_left",
        "auto_seat_climate_right",
        "auto_steering_wheel_heat",
        "battery_heater",
        "battery_heater_no_power",
        "bioweapon_mode_on",
        "cabin_overheat_protection",
        "cabin_overheat_protection_actively_cooling",
        "climate_keeper_mode",
        "cop_activation_temperature",
        "cop_not_running_reason",
        "defrost_mode",
        "driver_temp_setting",
        "fan_status",
        "hvac_auto_request",
        "inside_temp_celsius",
        "is_auto_conditioning_on",
        "is_climate_on",
        "is_front_defroster_on",
        "is_preconditioning",
        "is_rear_defroster_on",
        "left_temp_direction",
        "max_avail_temp_celsius",
        "min_avail_temp_celsius",
        "outside_temp_celsius",
        "passenger_temp_setting",
        "remote_heater_control_enabled",
        "right_temp_direction",
        "seat_fan_front_left",
        "seat_fan_front_right",
        "seat_heater_left",
        "seat_heater_rear_center",
        "seat_heater_rear_left",
        "seat_heater_rear_left_back",
        "seat_heater_rear_right",
        "seat_heater_rear_right_back",
        "seat_heater_right",
        "seat_heater_third_row_left",
        "seat_heater_third_row_right",
        "side_mirror_heaters",
        "steering_wheel_heat_level",
        "steering_wheel_heater",
        "supports_fan_only_cabin_overheat_protection",
        "timestamp",
        "wiper_blade_heater",
    )

    class HvacAutoRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HvacAutoRequestOn: _ClassVar[ClimateState.HvacAutoRequest]
        HvacAutoRequestOverride: _ClassVar[ClimateState.HvacAutoRequest]

    HvacAutoRequestOn: ClimateState.HvacAutoRequest
    HvacAutoRequestOverride: ClimateState.HvacAutoRequest

    class CabinOverheatProtection_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CabinOverheatProtectionOff: _ClassVar[ClimateState.CabinOverheatProtection_E]
        CabinOverheatProtectionOn: _ClassVar[ClimateState.CabinOverheatProtection_E]
        CabinOverheatProtectionFanOnly: _ClassVar[
            ClimateState.CabinOverheatProtection_E
        ]

    CabinOverheatProtectionOff: ClimateState.CabinOverheatProtection_E
    CabinOverheatProtectionOn: ClimateState.CabinOverheatProtection_E
    CabinOverheatProtectionFanOnly: ClimateState.CabinOverheatProtection_E

    class SeatHeaterLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeatHeaterLevelOff: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelLow: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelMed: _ClassVar[ClimateState.SeatHeaterLevel_E]
        SeatHeaterLevelHigh: _ClassVar[ClimateState.SeatHeaterLevel_E]

    SeatHeaterLevelOff: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelLow: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelMed: ClimateState.SeatHeaterLevel_E
    SeatHeaterLevelHigh: ClimateState.SeatHeaterLevel_E

    class SeatCoolingLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SeatCoolingLevelOff: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelLow: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelMed: _ClassVar[ClimateState.SeatCoolingLevel_E]
        SeatCoolingLevelHigh: _ClassVar[ClimateState.SeatCoolingLevel_E]

    SeatCoolingLevelOff: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelLow: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelMed: ClimateState.SeatCoolingLevel_E
    SeatCoolingLevelHigh: ClimateState.SeatCoolingLevel_E

    class CopActivationTemp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CopActivationTempUnspecified: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempLow: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempMedium: _ClassVar[ClimateState.CopActivationTemp]
        CopActivationTempHigh: _ClassVar[ClimateState.CopActivationTemp]

    CopActivationTempUnspecified: ClimateState.CopActivationTemp
    CopActivationTempLow: ClimateState.CopActivationTemp
    CopActivationTempMedium: ClimateState.CopActivationTemp
    CopActivationTempHigh: ClimateState.CopActivationTemp

    class COPNotRunningReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COPNotRunningReasonNoReason: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonUserInteraction: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonEnergyConsumptionReached: _ClassVar[
            ClimateState.COPNotRunningReason
        ]
        COPNotRunningReasonTimeout: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonLowSolarLoad: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonFault: _ClassVar[ClimateState.COPNotRunningReason]
        COPNotRunningReasonCabinBelowThreshold: _ClassVar[
            ClimateState.COPNotRunningReason
        ]

    COPNotRunningReasonNoReason: ClimateState.COPNotRunningReason
    COPNotRunningReasonUserInteraction: ClimateState.COPNotRunningReason
    COPNotRunningReasonEnergyConsumptionReached: ClimateState.COPNotRunningReason
    COPNotRunningReasonTimeout: ClimateState.COPNotRunningReason
    COPNotRunningReasonLowSolarLoad: ClimateState.COPNotRunningReason
    COPNotRunningReasonFault: ClimateState.COPNotRunningReason
    COPNotRunningReasonCabinBelowThreshold: ClimateState.COPNotRunningReason

    class ClimateKeeperMode(_message.Message):
        __slots__ = ("Dog", "Off", "On", "Party", "Unknown")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        DOG_FIELD_NUMBER: _ClassVar[int]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        Unknown: _common_pb2.Void
        Off: _common_pb2.Void
        On: _common_pb2.Void
        Dog: _common_pb2.Void
        Party: _common_pb2.Void

        def __init__(
            self,
            Unknown: _common_pb2.Void | _Mapping | None = ...,
            Off: _common_pb2.Void | _Mapping | None = ...,
            On: _common_pb2.Void | _Mapping | None = ...,
            Dog: _common_pb2.Void | _Mapping | None = ...,
            Party: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class DefrostMode(_message.Message):
        __slots__ = ("Max", "Normal", "Off")
        OFF_FIELD_NUMBER: _ClassVar[int]
        NORMAL_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        Off: _common_pb2.Void
        Normal: _common_pb2.Void
        Max: _common_pb2.Void

        def __init__(
            self,
            Off: _common_pb2.Void | _Mapping | None = ...,
            Normal: _common_pb2.Void | _Mapping | None = ...,
            Max: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    INSIDE_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    OUTSIDE_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TEMP_SETTING_FIELD_NUMBER: _ClassVar[int]
    PASSENGER_TEMP_SETTING_FIELD_NUMBER: _ClassVar[int]
    LEFT_TEMP_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TEMP_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    IS_FRONT_DEFROSTER_ON_FIELD_NUMBER: _ClassVar[int]
    IS_REAR_DEFROSTER_ON_FIELD_NUMBER: _ClassVar[int]
    FAN_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_CLIMATE_ON_FIELD_NUMBER: _ClassVar[int]
    MIN_AVAIL_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    MAX_AVAIL_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_CENTER_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_RIGHT_BACK_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_REAR_LEFT_BACK_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_THIRD_ROW_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_HEATER_THIRD_ROW_LEFT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_HEATER_FIELD_NUMBER: _ClassVar[int]
    BATTERY_HEATER_NO_POWER_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_HEATER_FIELD_NUMBER: _ClassVar[int]
    WIPER_BLADE_HEATER_FIELD_NUMBER: _ClassVar[int]
    SIDE_MIRROR_HEATERS_FIELD_NUMBER: _ClassVar[int]
    IS_PRECONDITIONING_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HEATER_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_KEEPER_MODE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BIOWEAPON_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    DEFROST_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_CONDITIONING_ON_FIELD_NUMBER: _ClassVar[int]
    AUTO_SEAT_CLIMATE_LEFT_FIELD_NUMBER: _ClassVar[int]
    AUTO_SEAT_CLIMATE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
    SEAT_FAN_FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FAN_ONLY_CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CABIN_OVERHEAT_PROTECTION_ACTIVELY_COOLING_FIELD_NUMBER: _ClassVar[int]
    COP_ACTIVATION_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    AUTO_STEERING_WHEEL_HEAT_FIELD_NUMBER: _ClassVar[int]
    STEERING_WHEEL_HEAT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    HVAC_AUTO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COP_NOT_RUNNING_REASON_FIELD_NUMBER: _ClassVar[int]
    inside_temp_celsius: float
    outside_temp_celsius: float
    driver_temp_setting: float
    passenger_temp_setting: float
    left_temp_direction: int
    right_temp_direction: int
    is_front_defroster_on: bool
    is_rear_defroster_on: bool
    fan_status: int
    is_climate_on: bool
    min_avail_temp_celsius: float
    max_avail_temp_celsius: float
    seat_heater_left: int
    seat_heater_right: int
    seat_heater_rear_left: int
    seat_heater_rear_right: int
    seat_heater_rear_center: int
    seat_heater_rear_right_back: int
    seat_heater_rear_left_back: int
    seat_heater_third_row_right: int
    seat_heater_third_row_left: int
    battery_heater: bool
    battery_heater_no_power: bool
    steering_wheel_heater: bool
    wiper_blade_heater: bool
    side_mirror_heaters: bool
    is_preconditioning: bool
    remote_heater_control_enabled: bool
    climate_keeper_mode: ClimateState.ClimateKeeperMode
    timestamp: _timestamp_pb2.Timestamp
    bioweapon_mode_on: bool
    defrost_mode: ClimateState.DefrostMode
    is_auto_conditioning_on: bool
    auto_seat_climate_left: bool
    auto_seat_climate_right: bool
    seat_fan_front_left: int
    seat_fan_front_right: int
    allow_cabin_overheat_protection: bool
    supports_fan_only_cabin_overheat_protection: bool
    cabin_overheat_protection: ClimateState.CabinOverheatProtection_E
    cabin_overheat_protection_actively_cooling: bool
    cop_activation_temperature: ClimateState.CopActivationTemp
    auto_steering_wheel_heat: bool
    steering_wheel_heat_level: _common_pb2.StwHeatLevel
    hvac_auto_request: ClimateState.HvacAutoRequest
    cop_not_running_reason: ClimateState.COPNotRunningReason

    def __init__(
        self,
        inside_temp_celsius: float | None = ...,
        outside_temp_celsius: float | None = ...,
        driver_temp_setting: float | None = ...,
        passenger_temp_setting: float | None = ...,
        left_temp_direction: int | None = ...,
        right_temp_direction: int | None = ...,
        is_front_defroster_on: bool = ...,
        is_rear_defroster_on: bool = ...,
        fan_status: int | None = ...,
        is_climate_on: bool = ...,
        min_avail_temp_celsius: float | None = ...,
        max_avail_temp_celsius: float | None = ...,
        seat_heater_left: int | None = ...,
        seat_heater_right: int | None = ...,
        seat_heater_rear_left: int | None = ...,
        seat_heater_rear_right: int | None = ...,
        seat_heater_rear_center: int | None = ...,
        seat_heater_rear_right_back: int | None = ...,
        seat_heater_rear_left_back: int | None = ...,
        seat_heater_third_row_right: int | None = ...,
        seat_heater_third_row_left: int | None = ...,
        battery_heater: bool = ...,
        battery_heater_no_power: bool = ...,
        steering_wheel_heater: bool = ...,
        wiper_blade_heater: bool = ...,
        side_mirror_heaters: bool = ...,
        is_preconditioning: bool = ...,
        remote_heater_control_enabled: bool = ...,
        climate_keeper_mode: ClimateState.ClimateKeeperMode | _Mapping | None = ...,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        bioweapon_mode_on: bool = ...,
        defrost_mode: ClimateState.DefrostMode | _Mapping | None = ...,
        is_auto_conditioning_on: bool = ...,
        auto_seat_climate_left: bool = ...,
        auto_seat_climate_right: bool = ...,
        seat_fan_front_left: int | None = ...,
        seat_fan_front_right: int | None = ...,
        allow_cabin_overheat_protection: bool = ...,
        supports_fan_only_cabin_overheat_protection: bool = ...,
        cabin_overheat_protection: ClimateState.CabinOverheatProtection_E
        | str
        | None = ...,
        cabin_overheat_protection_actively_cooling: bool = ...,
        cop_activation_temperature: ClimateState.CopActivationTemp | str | None = ...,
        auto_steering_wheel_heat: bool = ...,
        steering_wheel_heat_level: _common_pb2.StwHeatLevel | str | None = ...,
        hvac_auto_request: ClimateState.HvacAutoRequest | str | None = ...,
        cop_not_running_reason: ClimateState.COPNotRunningReason | str | None = ...,
    ) -> None: ...

class TirePressureState(_message.Message):
    __slots__ = (
        "timestamp",
        "tpms_hard_warning_fl",
        "tpms_hard_warning_fr",
        "tpms_hard_warning_rl",
        "tpms_hard_warning_rr",
        "tpms_last_seen_pressure_time_fl",
        "tpms_last_seen_pressure_time_fr",
        "tpms_last_seen_pressure_time_rl",
        "tpms_last_seen_pressure_time_rr",
        "tpms_pressure_fl",
        "tpms_pressure_fr",
        "tpms_pressure_rl",
        "tpms_pressure_rr",
        "tpms_rcp_front_value",
        "tpms_rcp_rear_value",
        "tpms_soft_warning_fl",
        "tpms_soft_warning_fr",
        "tpms_soft_warning_rl",
        "tpms_soft_warning_rr",
    )
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_PRESSURE_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_LAST_SEEN_PRESSURE_TIME_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_HARD_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_FR_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RL_FIELD_NUMBER: _ClassVar[int]
    TPMS_SOFT_WARNING_RR_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_FRONT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TPMS_RCP_REAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    tpms_pressure_fl: float
    tpms_pressure_fr: float
    tpms_pressure_rl: float
    tpms_pressure_rr: float
    tpms_last_seen_pressure_time_fl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_fr: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rl: _timestamp_pb2.Timestamp
    tpms_last_seen_pressure_time_rr: _timestamp_pb2.Timestamp
    tpms_hard_warning_fl: bool
    tpms_hard_warning_fr: bool
    tpms_hard_warning_rl: bool
    tpms_hard_warning_rr: bool
    tpms_soft_warning_fl: bool
    tpms_soft_warning_fr: bool
    tpms_soft_warning_rl: bool
    tpms_soft_warning_rr: bool
    tpms_rcp_front_value: float
    tpms_rcp_rear_value: float

    def __init__(
        self,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        tpms_pressure_fl: float | None = ...,
        tpms_pressure_fr: float | None = ...,
        tpms_pressure_rl: float | None = ...,
        tpms_pressure_rr: float | None = ...,
        tpms_last_seen_pressure_time_fl: _timestamp_pb2.Timestamp
        | _Mapping
        | None = ...,
        tpms_last_seen_pressure_time_fr: _timestamp_pb2.Timestamp
        | _Mapping
        | None = ...,
        tpms_last_seen_pressure_time_rl: _timestamp_pb2.Timestamp
        | _Mapping
        | None = ...,
        tpms_last_seen_pressure_time_rr: _timestamp_pb2.Timestamp
        | _Mapping
        | None = ...,
        tpms_hard_warning_fl: bool = ...,
        tpms_hard_warning_fr: bool = ...,
        tpms_hard_warning_rl: bool = ...,
        tpms_hard_warning_rr: bool = ...,
        tpms_soft_warning_fl: bool = ...,
        tpms_soft_warning_fr: bool = ...,
        tpms_soft_warning_rl: bool = ...,
        tpms_soft_warning_rr: bool = ...,
        tpms_rcp_front_value: float | None = ...,
        tpms_rcp_rear_value: float | None = ...,
    ) -> None: ...

class MediaState(_message.Message):
    __slots__ = (
        "audio_volume",
        "audio_volume_increment",
        "audio_volume_max",
        "media_playback_status",
        "now_playing_artist",
        "now_playing_source",
        "now_playing_title",
        "remote_control_enabled",
        "timestamp",
    )
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ARTIST_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_TITLE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_VOLUME_MAX_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PLAYBACK_STATUS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    remote_control_enabled: bool
    now_playing_artist: str
    now_playing_title: str
    audio_volume: float
    audio_volume_increment: float
    audio_volume_max: float
    now_playing_source: MediaSourceType
    media_playback_status: _common_pb2.MediaPlaybackStatus

    def __init__(
        self,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        remote_control_enabled: bool = ...,
        now_playing_artist: str | None = ...,
        now_playing_title: str | None = ...,
        audio_volume: float | None = ...,
        audio_volume_increment: float | None = ...,
        audio_volume_max: float | None = ...,
        now_playing_source: MediaSourceType | str | None = ...,
        media_playback_status: _common_pb2.MediaPlaybackStatus | str | None = ...,
    ) -> None: ...

class MediaDetailState(_message.Message):
    __slots__ = (
        "a2dp_source_name",
        "now_playing_album",
        "now_playing_duration",
        "now_playing_elapsed",
        "now_playing_source_string",
        "now_playing_station",
        "timestamp",
    )
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_DURATION_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ELAPSED_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_SOURCE_STRING_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_ALBUM_FIELD_NUMBER: _ClassVar[int]
    NOW_PLAYING_STATION_FIELD_NUMBER: _ClassVar[int]
    A2DP_SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    now_playing_duration: int
    now_playing_elapsed: int
    now_playing_source_string: str
    now_playing_album: str
    now_playing_station: str
    a2dp_source_name: str

    def __init__(
        self,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        now_playing_duration: int | None = ...,
        now_playing_elapsed: int | None = ...,
        now_playing_source_string: str | None = ...,
        now_playing_album: str | None = ...,
        now_playing_station: str | None = ...,
        a2dp_source_name: str | None = ...,
    ) -> None: ...

class ShiftState(_message.Message):
    __slots__ = ("D", "Invalid", "N", "P", "R", "SNA")
    INVALID_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    SNA_FIELD_NUMBER: _ClassVar[int]
    Invalid: _common_pb2.Void
    P: _common_pb2.Void
    R: _common_pb2.Void
    N: _common_pb2.Void
    D: _common_pb2.Void
    SNA: _common_pb2.Void

    def __init__(
        self,
        Invalid: _common_pb2.Void | _Mapping | None = ...,
        P: _common_pb2.Void | _Mapping | None = ...,
        R: _common_pb2.Void | _Mapping | None = ...,
        N: _common_pb2.Void | _Mapping | None = ...,
        D: _common_pb2.Void | _Mapping | None = ...,
        SNA: _common_pb2.Void | _Mapping | None = ...,
    ) -> None: ...
