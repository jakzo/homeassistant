"""Constants for the Tesla fleet push integration."""

from datetime import timedelta
from enum import StrEnum
import logging

from .tesla_fleet_api.const import Scope

API_TIMEOUT = 20
API_REFRESH = timedelta(minutes=1)

DOMAIN = "tesla_fleet_push"
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CONF_AUDENCE = "audience"
CONF_INSTANCE_DOMAIN = "instance_domain"
CONF_DOMAIN = "domain"

AUDIENCE_DEFAULT = "https://fleet-api.prd.na.vn.cloud.tesla.com"
AUDIENCES = [
    AUDIENCE_DEFAULT,
    "https://fleet-api.prd.eu.vn.cloud.tesla.com",
    "https://fleet-api.prd.cn.vn.cloud.tesla.com",
]

LOGGER = logging.getLogger(__package__)

CLIENT_ID = "71b813eb-4a2e-483a-b831-4dec5cb9bf0d"
AUTHORIZE_URL = "https://auth.tesla.com/oauth2/v3/authorize"
TOKEN_URL = "https://auth.tesla.com/oauth2/v3/token"

SCOPES = [
    Scope.OPENID,
    Scope.OFFLINE_ACCESS,
    Scope.VEHICLE_DEVICE_DATA,
    Scope.VEHICLE_LOCATION,
    Scope.VEHICLE_CMDS,
    Scope.VEHICLE_CHARGING_CMDS,
    Scope.ENERGY_DEVICE_DATA,
    Scope.ENERGY_CMDS,
]

MODELS = {
    "S": "Model S",
    "3": "Model 3",
    "X": "Model X",
    "Y": "Model Y",
    "C": "Cybertruck",
    "T": "Tesla Semi",
}


class TeslaFleetState(StrEnum):
    """Teslemetry Vehicle States."""

    ONLINE = "online"
    ASLEEP = "asleep"
    OFFLINE = "offline"
