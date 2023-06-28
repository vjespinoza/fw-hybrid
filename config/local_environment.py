from config.constants import EMPTY
from utilities.utils import get_variable


class LocalEnvironment:
    def __init__(self) -> None:
        self._COMPONENT = get_variable("COMPONENT")
        self._EXECUTION = get_variable("EXECUTION")
        self._BROWSER = get_variable("BROWSER")
        self._RESOLUTION = get_variable("RESOLUTION")
        self._APP_PLATFORM = get_variable("APP_PLATFORM")
        self._SL_USERNAME = get_variable("SL_USERNAME")
        self._SL_ACCESSKEY = get_variable("SL_ACCESSKEY")

    def get_component(self) -> str:
        return self._COMPONENT or "web"

    def get_execution(self) -> str:
        return self._EXECUTION or "local"

    def get_browser(self) -> str:
        return self._BROWSER or "chrome"

    def get_resolution(self) -> str:
        return self._RESOLUTION or "desktop"

    def get_app_platform(self) -> str:
        return self._APP_PLATFORM

    def get_username(self) -> str:
        return self._SL_USERNAME

    def get_accesskey(self) -> str:
        return self._SL_ACCESSKEY

    def is_mobile(self) -> bool:
        return self.get_resolution() != "desktop"

    def check_app_environment(self) -> bool:
        app_vars = {
            "component": self.get_component(),
            "execution": self.get_execution(),
            "app_platform": self.get_app_platform(),
        }
        return all(value != EMPTY for value in app_vars.values())

    def check_web_environment(self) -> bool:
        web_vars = {
            "browser": self.get_browser(),
            "resolution": self.get_resolution(),
            "execution": self.get_execution(),
            "component": self.get_component(),
        }
        return all(value != EMPTY for value in web_vars.values())
