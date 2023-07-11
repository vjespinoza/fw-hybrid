from typing import Callable

from appium import webdriver as awd
from selenium import webdriver as swd
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.constants import DESKTOP
from config.driver.driver_options import chrome_options, firefox_options

_BASE_URL = 'https://youtube.com/'
_APPIUM_SERVER = 'https://webdriver.io/'
_SAUCELABS_SERVER = 'https://ondemand.eu-central-1.saucelabs.com:443/wd/hub'

_DRIVERS = {
    "local-chrome": lambda opts: swd.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=opts),
    "local-firefox": lambda opts: swd.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=opts),
    "local-android": lambda opts: awd.webdriver.WebDriver(
        command_executor=_APPIUM_SERVER, options=opts),
    "remote-web": lambda opts: swd.Remote(
        command_executor=_SAUCELABS_SERVER, options=opts),
    "remote-app": lambda opts: awd.webdriver.WebDriver(
        command_executor=_SAUCELABS_SERVER, options=opts)
}

_DRIVER_OPTIONS = {
    "chrome": lambda is_local, screen_size: chrome_options(
        is_local=is_local, screen_size=screen_size),
    "firefox": lambda is_local, screen_size: firefox_options(
        is_local=is_local, screen_size=screen_size)
}


def get_driver(
        component: str,
        name: str,
        size: str,
        is_local: bool
) -> WebDriver:
    """
    Gets the required driver instance based on the args received
    :param component: Type of component (Web or App)
    :param name: name of the browser or app OS
    :param size: screen size
    :param is_local: execution type boolean (local or remote)
    :return:
    """
    if is_local:
        local_driver: Callable[[BaseOptions], WebDriver] = _DRIVERS[f'local-{name}']
        dvr = local_driver(_get_options(name=name, is_local=is_local, screen_size=size))
        if size == DESKTOP:
            dvr.maximize_window()
        return dvr
    else:
        remote_driver: Callable[[BaseOptions], WebDriver] = _DRIVERS[f'remote-{component}']
        return remote_driver(_get_options(name=name, is_local=is_local, screen_size=size))


def _get_options(name: str, is_local: bool, screen_size: str) -> BaseOptions:
    options_caller: Callable[[bool, str], BaseOptions] = _DRIVER_OPTIONS[name]
    options = options_caller(is_local, screen_size)
    return options

# if __name__ == '__main__':
#     def myfunc(name: str = 'test'):
#         print(f'Hello {name}!')
#
#
#     myfunc()
#     myfunc("Vic")
