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
import signatures_pb2 as _signatures_pb2
import vehicle_pb2 as _vehicle_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class OperationStatus_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATIONSTATUS_OK: _ClassVar[OperationStatus_E]
    OPERATIONSTATUS_ERROR: _ClassVar[OperationStatus_E]

OPERATIONSTATUS_OK: OperationStatus_E
OPERATIONSTATUS_ERROR: OperationStatus_E

class Action(_message.Message):
    __slots__ = ("vehicleAction",)
    VEHICLEACTION_FIELD_NUMBER: _ClassVar[int]
    vehicleAction: VehicleAction

    def __init__(
        self, vehicleAction: VehicleAction | _Mapping | None = ...
    ) -> None: ...

class VehicleAction(_message.Message):
    __slots__ = (
        "addChargeScheduleAction",
        "addPreconditionScheduleAction",
        "autoSeatClimateAction",
        "batchRemoveChargeSchedulesAction",
        "batchRemovePreconditionSchedulesAction",
        "chargePortDoorClose",
        "chargePortDoorOpen",
        "chargingSetLimitAction",
        "chargingStartStopAction",
        "drivingClearSpeedLimitPinAction",
        "drivingSetSpeedLimitAction",
        "drivingSpeedLimitAction",
        "eraseUserDataAction",
        "getNearbyChargingSites",
        "getVehicleData",
        "guestModeAction",
        "hvacAutoAction",
        "hvacBioweaponModeAction",
        "hvacClimateKeeperAction",
        "hvacSeatCoolerActions",
        "hvacSeatHeaterActions",
        "hvacSetPreconditioningMaxAction",
        "hvacSteeringWheelHeaterAction",
        "hvacTemperatureAdjustmentAction",
        "mediaNextFavorite",
        "mediaNextTrack",
        "mediaPlayAction",
        "mediaPreviousFavorite",
        "mediaPreviousTrack",
        "mediaUpdateVolume",
        "ping",
        "removeChargeScheduleAction",
        "removePreconditionScheduleAction",
        "scheduledChargingAction",
        "scheduledDepartureAction",
        "setCabinOverheatProtectionAction",
        "setChargingAmpsAction",
        "setCopTempAction",
        "setVehicleNameAction",
        "vehicleControlCancelSoftwareUpdateAction",
        "vehicleControlFlashLightsAction",
        "vehicleControlHonkHornAction",
        "vehicleControlResetPinToDriveAction",
        "vehicleControlResetValetPinAction",
        "vehicleControlScheduleSoftwareUpdateAction",
        "vehicleControlSetPinToDriveAction",
        "vehicleControlSetSentryModeAction",
        "vehicleControlSetValetModeAction",
        "vehicleControlSunroofOpenCloseAction",
        "vehicleControlTriggerHomelinkAction",
        "vehicleControlWindowAction",
    )
    GETVEHICLEDATA_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSETLIMITACTION_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSTARTSTOPACTION_FIELD_NUMBER: _ClassVar[int]
    DRIVINGCLEARSPEEDLIMITPINACTION_FIELD_NUMBER: _ClassVar[int]
    DRIVINGSETSPEEDLIMITACTION_FIELD_NUMBER: _ClassVar[int]
    DRIVINGSPEEDLIMITACTION_FIELD_NUMBER: _ClassVar[int]
    HVACAUTOACTION_FIELD_NUMBER: _ClassVar[int]
    HVACSETPRECONDITIONINGMAXACTION_FIELD_NUMBER: _ClassVar[int]
    HVACSTEERINGWHEELHEATERACTION_FIELD_NUMBER: _ClassVar[int]
    HVACTEMPERATUREADJUSTMENTACTION_FIELD_NUMBER: _ClassVar[int]
    MEDIAPLAYACTION_FIELD_NUMBER: _ClassVar[int]
    MEDIAUPDATEVOLUME_FIELD_NUMBER: _ClassVar[int]
    MEDIANEXTFAVORITE_FIELD_NUMBER: _ClassVar[int]
    MEDIAPREVIOUSFAVORITE_FIELD_NUMBER: _ClassVar[int]
    MEDIANEXTTRACK_FIELD_NUMBER: _ClassVar[int]
    MEDIAPREVIOUSTRACK_FIELD_NUMBER: _ClassVar[int]
    GETNEARBYCHARGINGSITES_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLCANCELSOFTWAREUPDATEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLFLASHLIGHTSACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLHONKHORNACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLRESETVALETPINACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLSCHEDULESOFTWAREUPDATEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLSETSENTRYMODEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLSETVALETMODEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLSUNROOFOPENCLOSEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLTRIGGERHOMELINKACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLWINDOWACTION_FIELD_NUMBER: _ClassVar[int]
    HVACBIOWEAPONMODEACTION_FIELD_NUMBER: _ClassVar[int]
    HVACSEATHEATERACTIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDCHARGINGACTION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDDEPARTUREACTION_FIELD_NUMBER: _ClassVar[int]
    SETCHARGINGAMPSACTION_FIELD_NUMBER: _ClassVar[int]
    HVACCLIMATEKEEPERACTION_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    AUTOSEATCLIMATEACTION_FIELD_NUMBER: _ClassVar[int]
    HVACSEATCOOLERACTIONS_FIELD_NUMBER: _ClassVar[int]
    SETCABINOVERHEATPROTECTIONACTION_FIELD_NUMBER: _ClassVar[int]
    SETVEHICLENAMEACTION_FIELD_NUMBER: _ClassVar[int]
    CHARGEPORTDOORCLOSE_FIELD_NUMBER: _ClassVar[int]
    CHARGEPORTDOOROPEN_FIELD_NUMBER: _ClassVar[int]
    GUESTMODEACTION_FIELD_NUMBER: _ClassVar[int]
    SETCOPTEMPACTION_FIELD_NUMBER: _ClassVar[int]
    ERASEUSERDATAACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLSETPINTODRIVEACTION_FIELD_NUMBER: _ClassVar[int]
    VEHICLECONTROLRESETPINTODRIVEACTION_FIELD_NUMBER: _ClassVar[int]
    ADDCHARGESCHEDULEACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVECHARGESCHEDULEACTION_FIELD_NUMBER: _ClassVar[int]
    ADDPRECONDITIONSCHEDULEACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVEPRECONDITIONSCHEDULEACTION_FIELD_NUMBER: _ClassVar[int]
    BATCHREMOVEPRECONDITIONSCHEDULESACTION_FIELD_NUMBER: _ClassVar[int]
    BATCHREMOVECHARGESCHEDULESACTION_FIELD_NUMBER: _ClassVar[int]
    getVehicleData: GetVehicleData
    chargingSetLimitAction: ChargingSetLimitAction
    chargingStartStopAction: ChargingStartStopAction
    drivingClearSpeedLimitPinAction: DrivingClearSpeedLimitPinAction
    drivingSetSpeedLimitAction: DrivingSetSpeedLimitAction
    drivingSpeedLimitAction: DrivingSpeedLimitAction
    hvacAutoAction: HvacAutoAction
    hvacSetPreconditioningMaxAction: HvacSetPreconditioningMaxAction
    hvacSteeringWheelHeaterAction: HvacSteeringWheelHeaterAction
    hvacTemperatureAdjustmentAction: HvacTemperatureAdjustmentAction
    mediaPlayAction: MediaPlayAction
    mediaUpdateVolume: MediaUpdateVolume
    mediaNextFavorite: MediaNextFavorite
    mediaPreviousFavorite: MediaPreviousFavorite
    mediaNextTrack: MediaNextTrack
    mediaPreviousTrack: MediaPreviousTrack
    getNearbyChargingSites: GetNearbyChargingSites
    vehicleControlCancelSoftwareUpdateAction: VehicleControlCancelSoftwareUpdateAction
    vehicleControlFlashLightsAction: VehicleControlFlashLightsAction
    vehicleControlHonkHornAction: VehicleControlHonkHornAction
    vehicleControlResetValetPinAction: VehicleControlResetValetPinAction
    vehicleControlScheduleSoftwareUpdateAction: (
        VehicleControlScheduleSoftwareUpdateAction
    )
    vehicleControlSetSentryModeAction: VehicleControlSetSentryModeAction
    vehicleControlSetValetModeAction: VehicleControlSetValetModeAction
    vehicleControlSunroofOpenCloseAction: VehicleControlSunroofOpenCloseAction
    vehicleControlTriggerHomelinkAction: VehicleControlTriggerHomelinkAction
    vehicleControlWindowAction: VehicleControlWindowAction
    hvacBioweaponModeAction: HvacBioweaponModeAction
    hvacSeatHeaterActions: HvacSeatHeaterActions
    scheduledChargingAction: ScheduledChargingAction
    scheduledDepartureAction: ScheduledDepartureAction
    setChargingAmpsAction: SetChargingAmpsAction
    hvacClimateKeeperAction: HvacClimateKeeperAction
    ping: Ping
    autoSeatClimateAction: AutoSeatClimateAction
    hvacSeatCoolerActions: HvacSeatCoolerActions
    setCabinOverheatProtectionAction: SetCabinOverheatProtectionAction
    setVehicleNameAction: SetVehicleNameAction
    chargePortDoorClose: ChargePortDoorClose
    chargePortDoorOpen: ChargePortDoorOpen
    guestModeAction: _vehicle_pb2.VehicleState.GuestMode
    setCopTempAction: SetCopTempAction
    eraseUserDataAction: EraseUserDataAction
    vehicleControlSetPinToDriveAction: VehicleControlSetPinToDriveAction
    vehicleControlResetPinToDriveAction: VehicleControlResetPinToDriveAction
    addChargeScheduleAction: _common_pb2.ChargeSchedule
    removeChargeScheduleAction: RemoveChargeScheduleAction
    addPreconditionScheduleAction: _common_pb2.PreconditionSchedule
    removePreconditionScheduleAction: RemovePreconditionScheduleAction
    batchRemovePreconditionSchedulesAction: BatchRemovePreconditionSchedulesAction
    batchRemoveChargeSchedulesAction: BatchRemoveChargeSchedulesAction

    def __init__(
        self,
        getVehicleData: GetVehicleData | _Mapping | None = ...,
        chargingSetLimitAction: ChargingSetLimitAction | _Mapping | None = ...,
        chargingStartStopAction: ChargingStartStopAction | _Mapping | None = ...,
        drivingClearSpeedLimitPinAction: DrivingClearSpeedLimitPinAction
        | _Mapping
        | None = ...,
        drivingSetSpeedLimitAction: DrivingSetSpeedLimitAction | _Mapping | None = ...,
        drivingSpeedLimitAction: DrivingSpeedLimitAction | _Mapping | None = ...,
        hvacAutoAction: HvacAutoAction | _Mapping | None = ...,
        hvacSetPreconditioningMaxAction: HvacSetPreconditioningMaxAction
        | _Mapping
        | None = ...,
        hvacSteeringWheelHeaterAction: HvacSteeringWheelHeaterAction
        | _Mapping
        | None = ...,
        hvacTemperatureAdjustmentAction: HvacTemperatureAdjustmentAction
        | _Mapping
        | None = ...,
        mediaPlayAction: MediaPlayAction | _Mapping | None = ...,
        mediaUpdateVolume: MediaUpdateVolume | _Mapping | None = ...,
        mediaNextFavorite: MediaNextFavorite | _Mapping | None = ...,
        mediaPreviousFavorite: MediaPreviousFavorite | _Mapping | None = ...,
        mediaNextTrack: MediaNextTrack | _Mapping | None = ...,
        mediaPreviousTrack: MediaPreviousTrack | _Mapping | None = ...,
        getNearbyChargingSites: GetNearbyChargingSites | _Mapping | None = ...,
        vehicleControlCancelSoftwareUpdateAction: VehicleControlCancelSoftwareUpdateAction
        | _Mapping
        | None = ...,
        vehicleControlFlashLightsAction: VehicleControlFlashLightsAction
        | _Mapping
        | None = ...,
        vehicleControlHonkHornAction: VehicleControlHonkHornAction
        | _Mapping
        | None = ...,
        vehicleControlResetValetPinAction: VehicleControlResetValetPinAction
        | _Mapping
        | None = ...,
        vehicleControlScheduleSoftwareUpdateAction: VehicleControlScheduleSoftwareUpdateAction
        | _Mapping
        | None = ...,
        vehicleControlSetSentryModeAction: VehicleControlSetSentryModeAction
        | _Mapping
        | None = ...,
        vehicleControlSetValetModeAction: VehicleControlSetValetModeAction
        | _Mapping
        | None = ...,
        vehicleControlSunroofOpenCloseAction: VehicleControlSunroofOpenCloseAction
        | _Mapping
        | None = ...,
        vehicleControlTriggerHomelinkAction: VehicleControlTriggerHomelinkAction
        | _Mapping
        | None = ...,
        vehicleControlWindowAction: VehicleControlWindowAction | _Mapping | None = ...,
        hvacBioweaponModeAction: HvacBioweaponModeAction | _Mapping | None = ...,
        hvacSeatHeaterActions: HvacSeatHeaterActions | _Mapping | None = ...,
        scheduledChargingAction: ScheduledChargingAction | _Mapping | None = ...,
        scheduledDepartureAction: ScheduledDepartureAction | _Mapping | None = ...,
        setChargingAmpsAction: SetChargingAmpsAction | _Mapping | None = ...,
        hvacClimateKeeperAction: HvacClimateKeeperAction | _Mapping | None = ...,
        ping: Ping | _Mapping | None = ...,
        autoSeatClimateAction: AutoSeatClimateAction | _Mapping | None = ...,
        hvacSeatCoolerActions: HvacSeatCoolerActions | _Mapping | None = ...,
        setCabinOverheatProtectionAction: SetCabinOverheatProtectionAction
        | _Mapping
        | None = ...,
        setVehicleNameAction: SetVehicleNameAction | _Mapping | None = ...,
        chargePortDoorClose: ChargePortDoorClose | _Mapping | None = ...,
        chargePortDoorOpen: ChargePortDoorOpen | _Mapping | None = ...,
        guestModeAction: _vehicle_pb2.VehicleState.GuestMode | _Mapping | None = ...,
        setCopTempAction: SetCopTempAction | _Mapping | None = ...,
        eraseUserDataAction: EraseUserDataAction | _Mapping | None = ...,
        vehicleControlSetPinToDriveAction: VehicleControlSetPinToDriveAction
        | _Mapping
        | None = ...,
        vehicleControlResetPinToDriveAction: VehicleControlResetPinToDriveAction
        | _Mapping
        | None = ...,
        addChargeScheduleAction: _common_pb2.ChargeSchedule | _Mapping | None = ...,
        removeChargeScheduleAction: RemoveChargeScheduleAction | _Mapping | None = ...,
        addPreconditionScheduleAction: _common_pb2.PreconditionSchedule
        | _Mapping
        | None = ...,
        removePreconditionScheduleAction: RemovePreconditionScheduleAction
        | _Mapping
        | None = ...,
        batchRemovePreconditionSchedulesAction: BatchRemovePreconditionSchedulesAction
        | _Mapping
        | None = ...,
        batchRemoveChargeSchedulesAction: BatchRemoveChargeSchedulesAction
        | _Mapping
        | None = ...,
    ) -> None: ...

class GetVehicleData(_message.Message):
    __slots__ = (
        "getChargeScheduleState",
        "getChargeState",
        "getClimateState",
        "getClosuresState",
        "getDriveState",
        "getLocationState",
        "getMediaDetailState",
        "getMediaState",
        "getParentalControlsState",
        "getPreconditioningScheduleState",
        "getSoftwareUpdateState",
        "getTirePressureState",
    )
    GETCHARGESTATE_FIELD_NUMBER: _ClassVar[int]
    GETCLIMATESTATE_FIELD_NUMBER: _ClassVar[int]
    GETDRIVESTATE_FIELD_NUMBER: _ClassVar[int]
    GETLOCATIONSTATE_FIELD_NUMBER: _ClassVar[int]
    GETCLOSURESSTATE_FIELD_NUMBER: _ClassVar[int]
    GETCHARGESCHEDULESTATE_FIELD_NUMBER: _ClassVar[int]
    GETPRECONDITIONINGSCHEDULESTATE_FIELD_NUMBER: _ClassVar[int]
    GETTIREPRESSURESTATE_FIELD_NUMBER: _ClassVar[int]
    GETMEDIASTATE_FIELD_NUMBER: _ClassVar[int]
    GETMEDIADETAILSTATE_FIELD_NUMBER: _ClassVar[int]
    GETSOFTWAREUPDATESTATE_FIELD_NUMBER: _ClassVar[int]
    GETPARENTALCONTROLSSTATE_FIELD_NUMBER: _ClassVar[int]
    getChargeState: GetChargeState
    getClimateState: GetClimateState
    getDriveState: GetDriveState
    getLocationState: GetLocationState
    getClosuresState: GetClosuresState
    getChargeScheduleState: GetChargeScheduleState
    getPreconditioningScheduleState: GetPreconditioningScheduleState
    getTirePressureState: GetTirePressureState
    getMediaState: GetMediaState
    getMediaDetailState: GetMediaDetailState
    getSoftwareUpdateState: GetSoftwareUpdateState
    getParentalControlsState: GetParentalControlsState

    def __init__(
        self,
        getChargeState: GetChargeState | _Mapping | None = ...,
        getClimateState: GetClimateState | _Mapping | None = ...,
        getDriveState: GetDriveState | _Mapping | None = ...,
        getLocationState: GetLocationState | _Mapping | None = ...,
        getClosuresState: GetClosuresState | _Mapping | None = ...,
        getChargeScheduleState: GetChargeScheduleState | _Mapping | None = ...,
        getPreconditioningScheduleState: GetPreconditioningScheduleState
        | _Mapping
        | None = ...,
        getTirePressureState: GetTirePressureState | _Mapping | None = ...,
        getMediaState: GetMediaState | _Mapping | None = ...,
        getMediaDetailState: GetMediaDetailState | _Mapping | None = ...,
        getSoftwareUpdateState: GetSoftwareUpdateState | _Mapping | None = ...,
        getParentalControlsState: GetParentalControlsState | _Mapping | None = ...,
    ) -> None: ...

class GetTirePressureState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetMediaState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetMediaDetailState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetSoftwareUpdateState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetChargeState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetClimateState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetDriveState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetLocationState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetClosuresState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetChargeScheduleState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetPreconditioningScheduleState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class GetParentalControlsState(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class EraseUserDataAction(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str

    def __init__(self, reason: str | None = ...) -> None: ...

class Response(_message.Message):
    __slots__ = (
        "actionStatus",
        "getNearbyChargingSites",
        "getSessionInfoResponse",
        "ping",
        "vehicleData",
    )
    ACTIONSTATUS_FIELD_NUMBER: _ClassVar[int]
    VEHICLEDATA_FIELD_NUMBER: _ClassVar[int]
    GETSESSIONINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETNEARBYCHARGINGSITES_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    actionStatus: ActionStatus
    vehicleData: _vehicle_pb2.VehicleData
    getSessionInfoResponse: _signatures_pb2.SessionInfo
    getNearbyChargingSites: NearbyChargingSites
    ping: Ping

    def __init__(
        self,
        actionStatus: ActionStatus | _Mapping | None = ...,
        vehicleData: _vehicle_pb2.VehicleData | _Mapping | None = ...,
        getSessionInfoResponse: _signatures_pb2.SessionInfo | _Mapping | None = ...,
        getNearbyChargingSites: NearbyChargingSites | _Mapping | None = ...,
        ping: Ping | _Mapping | None = ...,
    ) -> None: ...

class ActionStatus(_message.Message):
    __slots__ = ("result", "result_reason")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT_REASON_FIELD_NUMBER: _ClassVar[int]
    result: OperationStatus_E
    result_reason: ResultReason

    def __init__(
        self,
        result: OperationStatus_E | str | None = ...,
        result_reason: ResultReason | _Mapping | None = ...,
    ) -> None: ...

class ResultReason(_message.Message):
    __slots__ = ("plain_text",)
    PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    plain_text: str

    def __init__(self, plain_text: str | None = ...) -> None: ...

class EncryptedData(_message.Message):
    __slots__ = ("ciphertext", "field_number", "tag")
    FIELD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    field_number: int
    ciphertext: bytes
    tag: bytes

    def __init__(
        self,
        field_number: int | None = ...,
        ciphertext: bytes | None = ...,
        tag: bytes | None = ...,
    ) -> None: ...

class ChargingSetLimitAction(_message.Message):
    __slots__ = ("percent",)
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    percent: int

    def __init__(self, percent: int | None = ...) -> None: ...

class ChargingStartStopAction(_message.Message):
    __slots__ = ("start", "start_max_range", "start_standard", "stop", "unknown")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    START_STANDARD_FIELD_NUMBER: _ClassVar[int]
    START_MAX_RANGE_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    unknown: _common_pb2.Void
    start: _common_pb2.Void
    start_standard: _common_pb2.Void
    start_max_range: _common_pb2.Void
    stop: _common_pb2.Void

    def __init__(
        self,
        unknown: _common_pb2.Void | _Mapping | None = ...,
        start: _common_pb2.Void | _Mapping | None = ...,
        start_standard: _common_pb2.Void | _Mapping | None = ...,
        start_max_range: _common_pb2.Void | _Mapping | None = ...,
        stop: _common_pb2.Void | _Mapping | None = ...,
    ) -> None: ...

class DrivingClearSpeedLimitPinAction(_message.Message):
    __slots__ = ("pin",)
    PIN_FIELD_NUMBER: _ClassVar[int]
    pin: str

    def __init__(self, pin: str | None = ...) -> None: ...

class DrivingSetSpeedLimitAction(_message.Message):
    __slots__ = ("limit_mph",)
    LIMIT_MPH_FIELD_NUMBER: _ClassVar[int]
    limit_mph: float

    def __init__(self, limit_mph: float | None = ...) -> None: ...

class DrivingSpeedLimitAction(_message.Message):
    __slots__ = ("activate", "pin")
    ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    activate: bool
    pin: str

    def __init__(self, activate: bool = ..., pin: str | None = ...) -> None: ...

class HvacAutoAction(_message.Message):
    __slots__ = ("manual_override", "power_on")
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    MANUAL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    power_on: bool
    manual_override: bool

    def __init__(self, power_on: bool = ..., manual_override: bool = ...) -> None: ...

class HvacSeatHeaterActions(_message.Message):
    __slots__ = ("hvacSeatHeaterAction",)

    class HvacSeatHeaterAction(_message.Message):
        __slots__ = (
            "CAR_SEAT_FRONT_LEFT",
            "CAR_SEAT_FRONT_RIGHT",
            "CAR_SEAT_REAR_CENTER",
            "CAR_SEAT_REAR_LEFT",
            "CAR_SEAT_REAR_LEFT_BACK",
            "CAR_SEAT_REAR_RIGHT",
            "CAR_SEAT_REAR_RIGHT_BACK",
            "CAR_SEAT_THIRD_ROW_LEFT",
            "CAR_SEAT_THIRD_ROW_RIGHT",
            "CAR_SEAT_UNKNOWN",
            "SEAT_HEATER_HIGH",
            "SEAT_HEATER_LOW",
            "SEAT_HEATER_MED",
            "SEAT_HEATER_OFF",
            "SEAT_HEATER_UNKNOWN",
        )
        SEAT_HEATER_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        SEAT_HEATER_OFF_FIELD_NUMBER: _ClassVar[int]
        SEAT_HEATER_LOW_FIELD_NUMBER: _ClassVar[int]
        SEAT_HEATER_MED_FIELD_NUMBER: _ClassVar[int]
        SEAT_HEATER_HIGH_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_REAR_LEFT_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_REAR_LEFT_BACK_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_REAR_CENTER_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_REAR_RIGHT_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_REAR_RIGHT_BACK_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_THIRD_ROW_LEFT_FIELD_NUMBER: _ClassVar[int]
        CAR_SEAT_THIRD_ROW_RIGHT_FIELD_NUMBER: _ClassVar[int]
        SEAT_HEATER_UNKNOWN: _common_pb2.Void
        SEAT_HEATER_OFF: _common_pb2.Void
        SEAT_HEATER_LOW: _common_pb2.Void
        SEAT_HEATER_MED: _common_pb2.Void
        SEAT_HEATER_HIGH: _common_pb2.Void
        CAR_SEAT_UNKNOWN: _common_pb2.Void
        CAR_SEAT_FRONT_LEFT: _common_pb2.Void
        CAR_SEAT_FRONT_RIGHT: _common_pb2.Void
        CAR_SEAT_REAR_LEFT: _common_pb2.Void
        CAR_SEAT_REAR_LEFT_BACK: _common_pb2.Void
        CAR_SEAT_REAR_CENTER: _common_pb2.Void
        CAR_SEAT_REAR_RIGHT: _common_pb2.Void
        CAR_SEAT_REAR_RIGHT_BACK: _common_pb2.Void
        CAR_SEAT_THIRD_ROW_LEFT: _common_pb2.Void
        CAR_SEAT_THIRD_ROW_RIGHT: _common_pb2.Void

        def __init__(
            self,
            SEAT_HEATER_UNKNOWN: _common_pb2.Void | _Mapping | None = ...,
            SEAT_HEATER_OFF: _common_pb2.Void | _Mapping | None = ...,
            SEAT_HEATER_LOW: _common_pb2.Void | _Mapping | None = ...,
            SEAT_HEATER_MED: _common_pb2.Void | _Mapping | None = ...,
            SEAT_HEATER_HIGH: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_UNKNOWN: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_FRONT_LEFT: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_FRONT_RIGHT: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_REAR_LEFT: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_REAR_LEFT_BACK: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_REAR_CENTER: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_REAR_RIGHT: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_REAR_RIGHT_BACK: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_THIRD_ROW_LEFT: _common_pb2.Void | _Mapping | None = ...,
            CAR_SEAT_THIRD_ROW_RIGHT: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    HVACSEATHEATERACTION_FIELD_NUMBER: _ClassVar[int]
    hvacSeatHeaterAction: _containers.RepeatedCompositeFieldContainer[
        HvacSeatHeaterActions.HvacSeatHeaterAction
    ]

    def __init__(
        self,
        hvacSeatHeaterAction: _Iterable[
            HvacSeatHeaterActions.HvacSeatHeaterAction | _Mapping
        ]
        | None = ...,
    ) -> None: ...

class HvacSeatCoolerActions(_message.Message):
    __slots__ = ("hvacSeatCoolerAction",)

    class HvacSeatCoolerLevel_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HvacSeatCoolerLevel_Unknown: _ClassVar[
            HvacSeatCoolerActions.HvacSeatCoolerLevel_E
        ]
        HvacSeatCoolerLevel_Off: _ClassVar[HvacSeatCoolerActions.HvacSeatCoolerLevel_E]
        HvacSeatCoolerLevel_Low: _ClassVar[HvacSeatCoolerActions.HvacSeatCoolerLevel_E]
        HvacSeatCoolerLevel_Med: _ClassVar[HvacSeatCoolerActions.HvacSeatCoolerLevel_E]
        HvacSeatCoolerLevel_High: _ClassVar[HvacSeatCoolerActions.HvacSeatCoolerLevel_E]

    HvacSeatCoolerLevel_Unknown: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
    HvacSeatCoolerLevel_Off: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
    HvacSeatCoolerLevel_Low: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
    HvacSeatCoolerLevel_Med: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
    HvacSeatCoolerLevel_High: HvacSeatCoolerActions.HvacSeatCoolerLevel_E

    class HvacSeatCoolerPosition_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HvacSeatCoolerPosition_Unknown: _ClassVar[
            HvacSeatCoolerActions.HvacSeatCoolerPosition_E
        ]
        HvacSeatCoolerPosition_FrontLeft: _ClassVar[
            HvacSeatCoolerActions.HvacSeatCoolerPosition_E
        ]
        HvacSeatCoolerPosition_FrontRight: _ClassVar[
            HvacSeatCoolerActions.HvacSeatCoolerPosition_E
        ]

    HvacSeatCoolerPosition_Unknown: HvacSeatCoolerActions.HvacSeatCoolerPosition_E
    HvacSeatCoolerPosition_FrontLeft: HvacSeatCoolerActions.HvacSeatCoolerPosition_E
    HvacSeatCoolerPosition_FrontRight: HvacSeatCoolerActions.HvacSeatCoolerPosition_E

    class HvacSeatCoolerAction(_message.Message):
        __slots__ = ("seat_cooler_level", "seat_position")
        SEAT_COOLER_LEVEL_FIELD_NUMBER: _ClassVar[int]
        SEAT_POSITION_FIELD_NUMBER: _ClassVar[int]
        seat_cooler_level: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
        seat_position: HvacSeatCoolerActions.HvacSeatCoolerPosition_E

        def __init__(
            self,
            seat_cooler_level: HvacSeatCoolerActions.HvacSeatCoolerLevel_E
            | str
            | None = ...,
            seat_position: HvacSeatCoolerActions.HvacSeatCoolerPosition_E
            | str
            | None = ...,
        ) -> None: ...

    HVACSEATCOOLERACTION_FIELD_NUMBER: _ClassVar[int]
    hvacSeatCoolerAction: _containers.RepeatedCompositeFieldContainer[
        HvacSeatCoolerActions.HvacSeatCoolerAction
    ]

    def __init__(
        self,
        hvacSeatCoolerAction: _Iterable[
            HvacSeatCoolerActions.HvacSeatCoolerAction | _Mapping
        ]
        | None = ...,
    ) -> None: ...

class HvacSetPreconditioningMaxAction(_message.Message):
    __slots__ = ("manual_override", "manual_override_mode", "on")

    class ManualOverrideMode_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DogMode: _ClassVar[HvacSetPreconditioningMaxAction.ManualOverrideMode_E]
        Soc: _ClassVar[HvacSetPreconditioningMaxAction.ManualOverrideMode_E]
        Doors: _ClassVar[HvacSetPreconditioningMaxAction.ManualOverrideMode_E]

    DogMode: HvacSetPreconditioningMaxAction.ManualOverrideMode_E
    Soc: HvacSetPreconditioningMaxAction.ManualOverrideMode_E
    Doors: HvacSetPreconditioningMaxAction.ManualOverrideMode_E
    ON_FIELD_NUMBER: _ClassVar[int]
    MANUAL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_OVERRIDE_MODE_FIELD_NUMBER: _ClassVar[int]
    on: bool
    manual_override: bool
    manual_override_mode: _containers.RepeatedScalarFieldContainer[
        HvacSetPreconditioningMaxAction.ManualOverrideMode_E
    ]

    def __init__(
        self,
        on: bool = ...,
        manual_override: bool = ...,
        manual_override_mode: _Iterable[
            HvacSetPreconditioningMaxAction.ManualOverrideMode_E | str
        ]
        | None = ...,
    ) -> None: ...

class HvacSteeringWheelHeaterAction(_message.Message):
    __slots__ = ("power_on",)
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    power_on: bool

    def __init__(self, power_on: bool = ...) -> None: ...

class HvacTemperatureAdjustmentAction(_message.Message):
    __slots__ = (
        "absolute_celsius",
        "delta_celsius",
        "delta_percent",
        "driver_temp_celsius",
        "hvac_temperature_zone",
        "level",
        "passenger_temp_celsius",
    )

    class Temperature(_message.Message):
        __slots__ = ("TEMP_MAX", "TEMP_MIN", "TEMP_UNKNOWN")
        TEMP_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        TEMP_MIN_FIELD_NUMBER: _ClassVar[int]
        TEMP_MAX_FIELD_NUMBER: _ClassVar[int]
        TEMP_UNKNOWN: _common_pb2.Void
        TEMP_MIN: _common_pb2.Void
        TEMP_MAX: _common_pb2.Void

        def __init__(
            self,
            TEMP_UNKNOWN: _common_pb2.Void | _Mapping | None = ...,
            TEMP_MIN: _common_pb2.Void | _Mapping | None = ...,
            TEMP_MAX: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    class HvacTemperatureZone(_message.Message):
        __slots__ = (
            "TEMP_ZONE_FRONT_LEFT",
            "TEMP_ZONE_FRONT_RIGHT",
            "TEMP_ZONE_REAR",
            "TEMP_ZONE_UNKNOWN",
        )
        TEMP_ZONE_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        TEMP_ZONE_FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
        TEMP_ZONE_FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
        TEMP_ZONE_REAR_FIELD_NUMBER: _ClassVar[int]
        TEMP_ZONE_UNKNOWN: _common_pb2.Void
        TEMP_ZONE_FRONT_LEFT: _common_pb2.Void
        TEMP_ZONE_FRONT_RIGHT: _common_pb2.Void
        TEMP_ZONE_REAR: _common_pb2.Void

        def __init__(
            self,
            TEMP_ZONE_UNKNOWN: _common_pb2.Void | _Mapping | None = ...,
            TEMP_ZONE_FRONT_LEFT: _common_pb2.Void | _Mapping | None = ...,
            TEMP_ZONE_FRONT_RIGHT: _common_pb2.Void | _Mapping | None = ...,
            TEMP_ZONE_REAR: _common_pb2.Void | _Mapping | None = ...,
        ) -> None: ...

    DELTA_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    HVAC_TEMPERATURE_ZONE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    PASSENGER_TEMP_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    delta_celsius: float
    delta_percent: int
    absolute_celsius: float
    level: HvacTemperatureAdjustmentAction.Temperature
    hvac_temperature_zone: _containers.RepeatedCompositeFieldContainer[
        HvacTemperatureAdjustmentAction.HvacTemperatureZone
    ]
    driver_temp_celsius: float
    passenger_temp_celsius: float

    def __init__(
        self,
        delta_celsius: float | None = ...,
        delta_percent: int | None = ...,
        absolute_celsius: float | None = ...,
        level: HvacTemperatureAdjustmentAction.Temperature | _Mapping | None = ...,
        hvac_temperature_zone: _Iterable[
            HvacTemperatureAdjustmentAction.HvacTemperatureZone | _Mapping
        ]
        | None = ...,
        driver_temp_celsius: float | None = ...,
        passenger_temp_celsius: float | None = ...,
    ) -> None: ...

class GetNearbyChargingSites(_message.Message):
    __slots__ = ("count", "include_meta_data", "radius")
    INCLUDE_META_DATA_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    include_meta_data: bool
    radius: int
    count: int

    def __init__(
        self,
        include_meta_data: bool = ...,
        radius: int | None = ...,
        count: int | None = ...,
    ) -> None: ...

class NearbyChargingSites(_message.Message):
    __slots__ = ("congestion_sync_time_utc_secs", "superchargers", "timestamp")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUPERCHARGERS_FIELD_NUMBER: _ClassVar[int]
    CONGESTION_SYNC_TIME_UTC_SECS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    superchargers: _containers.RepeatedCompositeFieldContainer[Superchargers]
    congestion_sync_time_utc_secs: int

    def __init__(
        self,
        timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        superchargers: _Iterable[Superchargers | _Mapping] | None = ...,
        congestion_sync_time_utc_secs: int | None = ...,
    ) -> None: ...

class Superchargers(_message.Message):
    __slots__ = (
        "amenities",
        "available_stalls",
        "billing_info",
        "billing_time",
        "city",
        "country",
        "distance_miles",
        "district",
        "id",
        "location",
        "max_power_kw",
        "name",
        "out_of_order_stalls_names",
        "out_of_order_stalls_number",
        "postal_code",
        "site_closed",
        "state",
        "street_address",
        "total_stalls",
        "within_range",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    AMENITIES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_STALLS_FIELD_NUMBER: _ClassVar[int]
    BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    BILLING_TIME_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_MILES_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SITE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STALLS_FIELD_NUMBER: _ClassVar[int]
    WITHIN_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_POWER_KW_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_ORDER_STALLS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_ORDER_STALLS_NAMES_FIELD_NUMBER: _ClassVar[int]
    id: int
    amenities: str
    available_stalls: int
    billing_info: str
    billing_time: str
    city: str
    country: str
    distance_miles: float
    district: str
    location: _common_pb2.LatLong
    name: str
    postal_code: str
    site_closed: bool
    state: str
    street_address: str
    total_stalls: int
    within_range: bool
    max_power_kw: int
    out_of_order_stalls_number: int
    out_of_order_stalls_names: str

    def __init__(
        self,
        id: int | None = ...,
        amenities: str | None = ...,
        available_stalls: int | None = ...,
        billing_info: str | None = ...,
        billing_time: str | None = ...,
        city: str | None = ...,
        country: str | None = ...,
        distance_miles: float | None = ...,
        district: str | None = ...,
        location: _common_pb2.LatLong | _Mapping | None = ...,
        name: str | None = ...,
        postal_code: str | None = ...,
        site_closed: bool = ...,
        state: str | None = ...,
        street_address: str | None = ...,
        total_stalls: int | None = ...,
        within_range: bool = ...,
        max_power_kw: int | None = ...,
        out_of_order_stalls_number: int | None = ...,
        out_of_order_stalls_names: str | None = ...,
    ) -> None: ...

class MediaPlayAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class MediaUpdateVolume(_message.Message):
    __slots__ = ("volume_absolute_float", "volume_delta")
    VOLUME_DELTA_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ABSOLUTE_FLOAT_FIELD_NUMBER: _ClassVar[int]
    volume_delta: int
    volume_absolute_float: float

    def __init__(
        self, volume_delta: int | None = ..., volume_absolute_float: float | None = ...
    ) -> None: ...

class MediaNextFavorite(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class MediaPreviousFavorite(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class MediaNextTrack(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class MediaPreviousTrack(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class VehicleControlCancelSoftwareUpdateAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class VehicleControlFlashLightsAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class VehicleControlHonkHornAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class VehicleControlResetValetPinAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class VehicleControlScheduleSoftwareUpdateAction(_message.Message):
    __slots__ = ("offset_sec",)
    OFFSET_SEC_FIELD_NUMBER: _ClassVar[int]
    offset_sec: int

    def __init__(self, offset_sec: int | None = ...) -> None: ...

class VehicleControlSetSentryModeAction(_message.Message):
    __slots__ = ("on",)
    ON_FIELD_NUMBER: _ClassVar[int]
    on: bool

    def __init__(self, on: bool = ...) -> None: ...

class VehicleControlSetValetModeAction(_message.Message):
    __slots__ = ("on", "password")
    ON_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    on: bool
    password: str

    def __init__(self, on: bool = ..., password: str | None = ...) -> None: ...

class VehicleControlSunroofOpenCloseAction(_message.Message):
    __slots__ = ("absolute_level", "close", "delta_level", "open", "vent")
    ABSOLUTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DELTA_LEVEL_FIELD_NUMBER: _ClassVar[int]
    VENT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    absolute_level: int
    delta_level: int
    vent: _common_pb2.Void
    close: _common_pb2.Void
    open: _common_pb2.Void

    def __init__(
        self,
        absolute_level: int | None = ...,
        delta_level: int | None = ...,
        vent: _common_pb2.Void | _Mapping | None = ...,
        close: _common_pb2.Void | _Mapping | None = ...,
        open: _common_pb2.Void | _Mapping | None = ...,
    ) -> None: ...

class VehicleControlTriggerHomelinkAction(_message.Message):
    __slots__ = ("location", "token")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: _common_pb2.LatLong
    token: str

    def __init__(
        self,
        location: _common_pb2.LatLong | _Mapping | None = ...,
        token: str | None = ...,
    ) -> None: ...

class VehicleControlWindowAction(_message.Message):
    __slots__ = ("close", "unknown", "vent")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    VENT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    unknown: _common_pb2.Void
    vent: _common_pb2.Void
    close: _common_pb2.Void

    def __init__(
        self,
        unknown: _common_pb2.Void | _Mapping | None = ...,
        vent: _common_pb2.Void | _Mapping | None = ...,
        close: _common_pb2.Void | _Mapping | None = ...,
    ) -> None: ...

class HvacBioweaponModeAction(_message.Message):
    __slots__ = ("manual_override", "on")
    ON_FIELD_NUMBER: _ClassVar[int]
    MANUAL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    on: bool
    manual_override: bool

    def __init__(self, on: bool = ..., manual_override: bool = ...) -> None: ...

class AutoSeatClimateAction(_message.Message):
    __slots__ = ("carseat",)

    class AutoSeatPosition_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AutoSeatPosition_Unknown: _ClassVar[AutoSeatClimateAction.AutoSeatPosition_E]
        AutoSeatPosition_FrontLeft: _ClassVar[AutoSeatClimateAction.AutoSeatPosition_E]
        AutoSeatPosition_FrontRight: _ClassVar[AutoSeatClimateAction.AutoSeatPosition_E]

    AutoSeatPosition_Unknown: AutoSeatClimateAction.AutoSeatPosition_E
    AutoSeatPosition_FrontLeft: AutoSeatClimateAction.AutoSeatPosition_E
    AutoSeatPosition_FrontRight: AutoSeatClimateAction.AutoSeatPosition_E

    class CarSeat(_message.Message):
        __slots__ = ("on", "seat_position")
        ON_FIELD_NUMBER: _ClassVar[int]
        SEAT_POSITION_FIELD_NUMBER: _ClassVar[int]
        on: bool
        seat_position: AutoSeatClimateAction.AutoSeatPosition_E

        def __init__(
            self,
            on: bool = ...,
            seat_position: AutoSeatClimateAction.AutoSeatPosition_E | str | None = ...,
        ) -> None: ...

    CARSEAT_FIELD_NUMBER: _ClassVar[int]
    carseat: _containers.RepeatedCompositeFieldContainer[AutoSeatClimateAction.CarSeat]

    def __init__(
        self, carseat: _Iterable[AutoSeatClimateAction.CarSeat | _Mapping] | None = ...
    ) -> None: ...

class Ping(_message.Message):
    __slots__ = ("last_remote_timestamp", "local_timestamp", "ping_id")
    PING_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_REMOTE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ping_id: int
    local_timestamp: _timestamp_pb2.Timestamp
    last_remote_timestamp: _timestamp_pb2.Timestamp

    def __init__(
        self,
        ping_id: int | None = ...,
        local_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        last_remote_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class ScheduledChargingAction(_message.Message):
    __slots__ = ("charging_time", "enabled")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHARGING_TIME_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    charging_time: int

    def __init__(
        self, enabled: bool = ..., charging_time: int | None = ...
    ) -> None: ...

class ScheduledDepartureAction(_message.Message):
    __slots__ = (
        "departure_time",
        "enabled",
        "off_peak_charging_times",
        "off_peak_hours_end_time",
        "preconditioning_times",
    )
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_CHARGING_TIMES_FIELD_NUMBER: _ClassVar[int]
    OFF_PEAK_HOURS_END_TIME_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    departure_time: int
    preconditioning_times: _common_pb2.PreconditioningTimes
    off_peak_charging_times: _common_pb2.OffPeakChargingTimes
    off_peak_hours_end_time: int

    def __init__(
        self,
        enabled: bool = ...,
        departure_time: int | None = ...,
        preconditioning_times: _common_pb2.PreconditioningTimes | _Mapping | None = ...,
        off_peak_charging_times: _common_pb2.OffPeakChargingTimes
        | _Mapping
        | None = ...,
        off_peak_hours_end_time: int | None = ...,
    ) -> None: ...

class HvacClimateKeeperAction(_message.Message):
    __slots__ = ("ClimateKeeperAction", "manual_override")

    class ClimateKeeperAction_E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ClimateKeeperAction_Off: _ClassVar[
            HvacClimateKeeperAction.ClimateKeeperAction_E
        ]
        ClimateKeeperAction_On: _ClassVar[HvacClimateKeeperAction.ClimateKeeperAction_E]
        ClimateKeeperAction_Dog: _ClassVar[
            HvacClimateKeeperAction.ClimateKeeperAction_E
        ]
        ClimateKeeperAction_Camp: _ClassVar[
            HvacClimateKeeperAction.ClimateKeeperAction_E
        ]

    ClimateKeeperAction_Off: HvacClimateKeeperAction.ClimateKeeperAction_E
    ClimateKeeperAction_On: HvacClimateKeeperAction.ClimateKeeperAction_E
    ClimateKeeperAction_Dog: HvacClimateKeeperAction.ClimateKeeperAction_E
    ClimateKeeperAction_Camp: HvacClimateKeeperAction.ClimateKeeperAction_E
    CLIMATEKEEPERACTION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ClimateKeeperAction: HvacClimateKeeperAction.ClimateKeeperAction_E
    manual_override: bool

    def __init__(
        self,
        ClimateKeeperAction: HvacClimateKeeperAction.ClimateKeeperAction_E
        | str
        | None = ...,
        manual_override: bool = ...,
    ) -> None: ...

class SetChargingAmpsAction(_message.Message):
    __slots__ = ("charging_amps",)
    CHARGING_AMPS_FIELD_NUMBER: _ClassVar[int]
    charging_amps: int

    def __init__(self, charging_amps: int | None = ...) -> None: ...

class RemoveChargeScheduleAction(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: int | None = ...) -> None: ...

class BatchRemoveChargeSchedulesAction(_message.Message):
    __slots__ = ("home", "other", "work")
    HOME_FIELD_NUMBER: _ClassVar[int]
    WORK_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_NUMBER: _ClassVar[int]
    home: bool
    work: bool
    other: bool

    def __init__(
        self, home: bool = ..., work: bool = ..., other: bool = ...
    ) -> None: ...

class BatchRemovePreconditionSchedulesAction(_message.Message):
    __slots__ = ("home", "other", "work")
    HOME_FIELD_NUMBER: _ClassVar[int]
    WORK_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_NUMBER: _ClassVar[int]
    home: bool
    work: bool
    other: bool

    def __init__(
        self, home: bool = ..., work: bool = ..., other: bool = ...
    ) -> None: ...

class RemovePreconditionScheduleAction(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: int | None = ...) -> None: ...

class SetCabinOverheatProtectionAction(_message.Message):
    __slots__ = ("fan_only", "on")
    ON_FIELD_NUMBER: _ClassVar[int]
    FAN_ONLY_FIELD_NUMBER: _ClassVar[int]
    on: bool
    fan_only: bool

    def __init__(self, on: bool = ..., fan_only: bool = ...) -> None: ...

class SetVehicleNameAction(_message.Message):
    __slots__ = ("vehicleName",)
    VEHICLENAME_FIELD_NUMBER: _ClassVar[int]
    vehicleName: str

    def __init__(self, vehicleName: str | None = ...) -> None: ...

class ChargePortDoorClose(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class ChargePortDoorOpen(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...

class SetCopTempAction(_message.Message):
    __slots__ = ("copActivationTemp",)
    COPACTIVATIONTEMP_FIELD_NUMBER: _ClassVar[int]
    copActivationTemp: _vehicle_pb2.ClimateState.CopActivationTemp

    def __init__(
        self,
        copActivationTemp: _vehicle_pb2.ClimateState.CopActivationTemp
        | str
        | None = ...,
    ) -> None: ...

class VehicleControlSetPinToDriveAction(_message.Message):
    __slots__ = ("on", "password")
    ON_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    on: bool
    password: str

    def __init__(self, on: bool = ..., password: str | None = ...) -> None: ...

class VehicleControlResetPinToDriveAction(_message.Message):
    __slots__ = ()

    def __init__(self) -> None: ...
