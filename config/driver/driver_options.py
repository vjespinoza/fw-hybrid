from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.constants import DESKTOP
from config.driver.driver_helper import set_mobile_emulation, set_remote_options
from utilities.utils import browser_resolution


def chrome_options(is_local: bool = True, screen_size: str = DESKTOP) -> BaseOptions:
    opts = ChromeOptions()
    resolution = browser_resolution(screen_size)
    if is_local:
        opts.add_experimental_option(
            "mobileEmulation",
            set_mobile_emulation((resolution[0], resolution[1]), resolution[2]))
    else:
        set_remote_options(options=opts)
    return opts


def firefox_options(is_local: bool = True, screen_size: str = DESKTOP) -> BaseOptions:
    opts = FirefoxOptions()
    resolution = browser_resolution(screen_size)
    if is_local:
        opts.set_preference("general.useragent.override", resolution[2])
        opts.add_argument(argument=f"--width={resolution[0]}")
        opts.add_argument(argument=f"--height={resolution[1]}")
    else:
        set_remote_options(options=opts)
    return opts
