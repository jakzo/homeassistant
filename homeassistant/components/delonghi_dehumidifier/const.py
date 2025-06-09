"""Constants for the De'Longhi DDSX Dehumidifier (based on Ayla IOT) integration."""

from datetime import timedelta

API_TIMEOUT = 20
API_REFRESH = timedelta(minutes=1)

DOMAIN = "delonghi_dehumidifier"

CONF_REGION = "region"
CONF_EUROPE = "is_europe"
REGION_EU = "eu"
REGION_DEFAULT = "default"

COMFORT_APP_ID = "DeLonghiComfort2-mw-id"
COMFORT_APP_SECRET = "DeLonghiComfort2-Yg4miiqiNcf0Or-EhJwRh7ACfBY"

REGIONS = {REGION_EU: "Europe", REGION_DEFAULT: "Default"}
