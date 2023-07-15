from typing import Tuple

from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.constants import APK_FILE_LOCAL, DEVICE_NAME_LOCAL
from utilities.utils import browser_resolution


def chrome_options(is_local: bool, screen_size: str) -> BaseOptions:
    opts = ChromeOptions()
    resolution = browser_resolution(screen_size)
    if is_local:
        opts.add_experimental_option(
            "mobileEmulation",
            _set_mobile_emulation((resolution[0], resolution[1]), resolution[2]))
    else:
        _set_remote_options(options=opts)
    return opts


def firefox_options(is_local: bool, screen_size: str) -> BaseOptions:
    opts = FirefoxOptions()
    resolution = browser_resolution(screen_size)
    if is_local:
        opts.set_preference("general.useragent.override", resolution[2])
        # opts.add_argument(argument=f"--width={resolution[0]}")
        # opts.add_argument(argument=f"--height={resolution[1]}")
    else:
        _set_remote_options(options=opts)
    return opts


def android_options(is_local: bool) -> BaseOptions:
    opts = UiAutomator2Options()
    if is_local:
        _set_capabilities(options=opts)
    else:
        _set_remote_options(options=opts)
    return opts


def _set_remote_options(options: BaseOptions) -> None:
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    options.set_capability("sauce:options", "Implement helper func")


def _set_mobile_emulation(resolution: Tuple[int, int], user_agent: str) \
        -> dict[str, dict[str, int | float] | str]:
    return {
        "deviceMetrics": {
            "width": resolution[0],
            "height": resolution[1],
            "pixelRatio": 3.0,
        },
        "userAgent": user_agent
    }


def _set_capabilities(options: BaseOptions) -> None:
    options.set_capability("platformName", "Android")
    options.set_capability("appium:app", APK_FILE_LOCAL)
    options.set_capability("appium:deviceName", DEVICE_NAME_LOCAL)
    options.set_capability("appium:deviceOrientation", "portrait")
    options.set_capability("appium:platformVersion", "13.0")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:udid", "emulator-5554")
    options.set_capability("appium:appActivity", "com.wdiodemoapp.MainActivity")
