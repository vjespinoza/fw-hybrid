from config.constants import COMPONENT_WEB, EXECUTION_LOCAL, CHROME, DESKTOP
from utilities.utils import get_variable


class LocalEnvironment:
    def __init__(self) -> None:
        self._COMPONENT = get_variable("COMPONENT")  # web or app
        self._EXECUTION = get_variable("EXECUTION")  # local or remote
        self._PLATFORM_NAME = get_variable("PLATFORM_NAME")  # browser name or app OS
        self._SCREEN_SIZE = get_variable("SCREEN_SIZE")  # screen size
        self._SL_USERNAME = get_variable("SL_USERNAME")
        self._SL_ACCESSKEY = get_variable("SL_ACCESSKEY")

    def get_component(self) -> str:
        return self._COMPONENT or COMPONENT_WEB

    def get_execution(self) -> str:
        return self._EXECUTION or EXECUTION_LOCAL

    def get_platform_name(self) -> str:
        return self._PLATFORM_NAME or CHROME

    def get_scren_size(self) -> str:
        return self._SCREEN_SIZE or DESKTOP

    def get_username(self) -> str:
        return self._SL_USERNAME

    def get_accesskey(self) -> str:
        return self._SL_ACCESSKEY

    def is_mobile(self) -> bool:
        return self.get_scren_size() != "desktop"

    def is_local(self) -> bool:
        return self.get_execution() == "local"
