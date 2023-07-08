from typing import Callable

from appium import webdriver as awd
from selenium import webdriver as swd
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.driver.driver_options import chrome_options, firefox_options

_BASE_URL = 'https://youtube.com/'
_APPIUM_SERVER = 'https://webdriver.io/'
_SAUCELABS_SERVER = 'https://ondemand.eu-central-1.saucelabs.com:443/wd/hub'

_WEB_DRIVERS = {
    "local-chrome": lambda opts: swd.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=opts),
    "local-firefox": lambda opts: swd.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=opts),
    "remote": lambda opts: swd.Remote(command_executor=_SAUCELABS_SERVER, options=opts)
}

_APP_DRIVERS = {
    "local": lambda opts: awd.webdriver.WebDriver(
        command_executor=_APPIUM_SERVER, options=opts),
    "remote": lambda opts: awd.webdriver.WebDriver(
        command_executor=_SAUCELABS_SERVER, options=opts)
}

_DRIVER_OPTIONS = {
    "chrome": lambda is_local: chrome_options(is_local=is_local),
    "firefox": lambda is_local: firefox_options(is_local=is_local)
}


def get_web_driver(
        browser: str = 'chrome', is_local: bool = True
) -> WebDriver:
    """
    Gets the required driver instance based on the args received
    :param browser: name of the browser
    :param is_local: boolean that defines the type of execution
    :return:
    """
    if is_local:
        local_driver: Callable[[BaseOptions], WebDriver] = _WEB_DRIVERS[f'local-{browser}']
        return local_driver(_get_options(name=browser, is_local=is_local))
    else:
        remote_driver: Callable[[BaseOptions], WebDriver] = _WEB_DRIVERS['remote']
        return remote_driver(_get_options(name=browser, is_local=is_local))


def _get_options(name: str, is_local: bool) -> BaseOptions:
    options_caller: Callable[[bool], BaseOptions] = _DRIVER_OPTIONS[name]
    options = options_caller(is_local)
    return options

# if __name__ == '__main__':
#     d = get_web_driver(browser='firefox', is_local=True)
#     d.get(_BASE_URL)
#     d.close()
