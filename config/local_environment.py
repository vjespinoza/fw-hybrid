import os

from dotenv import load_dotenv

_DEFAULT_VALUES = {
    "platform": "chrome",
    "resolution": "fullscreen",
    "run_type": "local",
}


class LocalEnvironment:
    def __init__(self):
        load_dotenv()
        self._PLATFORM = os.getenv("PLATFORM").lower() or _DEFAULT_VALUES.get("platform")
        self._RESOLUTION = os.getenv("RESOLUTION").lower() or _DEFAULT_VALUES.get("resolution")
        self._RUN_TYPE = os.getenv("RUN_TYPE").lower() or _DEFAULT_VALUES.get("run_type")
        self._SL_USERNAME = os.getenv("SL_USERNAME")
        self._SL_ACCESSKEY = os.getenv("SL_ACCESSKEY")

    def get_platform(self):
        return self._PLATFORM

    def get_resolution(self):
        return self._RESOLUTION

    def get_run_type(self):
        return self._RUN_TYPE

    def is_local(self):
        return self._RUN_TYPE == "local"

    def is_responsive(self):
        return self._RESOLUTION != "fullscreen"

    def is_web(self):
        return self._PLATFORM != "android" and self._PLATFORM != ""

    def get_username(self):
        return self._SL_USERNAME

    def get_accesskey(self):
        return self._SL_ACCESSKEY
