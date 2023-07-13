from typing import Callable

from appium import webdriver as awd
from selenium import webdriver as swd
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.constants import DESKTOP, COMPONENT_WEB, COMPONENT_APP
from config.driver.driver_options import chrome_options, firefox_options, android_options

_BASE_URL = 'https://youtube.com/'
_APPIUM_SERVER = 'http://localhost:4723'
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

_WEB_DRIVER_OPTIONS = {
    "chrome": lambda is_local, screen_size: chrome_options(
        is_local=is_local, screen_size=screen_size),
    "firefox": lambda is_local, screen_size: firefox_options(
        is_local=is_local, screen_size=screen_size)
}


def get_driver(
        name: str, size: str, is_web: bool, is_local: bool
) -> WebDriver:
    """
    Gets the required driver instance based on the args received
    :param name: Name of the browser or app OS
    :param size: Screen size for web drivers
    :param is_web: Boolean defining type of component (web or app)
    :param is_local: Boolean defining type of execution (local or remote)
    :return: driver
    """

    options = _get_web_options(name=name, is_local=is_local, screen_size=size) \
        if is_web else _get_app_options(is_local=is_local)

    if is_local:
        local_driver: Callable[[BaseOptions], WebDriver] = _DRIVERS[f'local-{name}']
        dvr = local_driver(options)
        if size == DESKTOP:
            dvr.maximize_window()
        return dvr
    else:
        component = COMPONENT_WEB if is_web else COMPONENT_APP
        remote_driver: Callable[[BaseOptions], WebDriver] = _DRIVERS[f'remote-{component}']
        return remote_driver(options)


def _get_web_options(name: str, is_local: bool, screen_size: str) -> BaseOptions:
    options_caller: Callable[[bool, str], BaseOptions] = _WEB_DRIVER_OPTIONS[name]
    options = options_caller(is_local, screen_size)
    return options


def _get_app_options(is_local: bool) -> BaseOptions:
    return android_options(is_local=is_local)
