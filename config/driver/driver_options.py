from typing import Tuple

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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
        opts.add_argument(argument=f"--width={resolution[0]}")
        opts.add_argument(argument=f"--height={resolution[1]}")
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
