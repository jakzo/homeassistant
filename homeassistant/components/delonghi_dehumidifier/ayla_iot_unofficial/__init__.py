"""Python API for Ayla IoT devices"""

from .ayla_iot_unofficial import AylaApi, new_ayla_api
from .exc import (
    AylaAuthError,
    AylaAuthExpiringError,
    AylaError,
    AylaNotAuthedError,
    AylaReadOnlyPropertyError,
)

__version__ = "1.4.8"
