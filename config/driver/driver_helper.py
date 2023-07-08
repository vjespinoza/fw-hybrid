from typing import Tuple

from selenium.webdriver.common.options import BaseOptions


def set_remote_options(options: BaseOptions) -> None:
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    options.set_capability("sauce:options", "Implement helper func")


def set_mobile_emulation(resolution: Tuple[int, int], user_agent: str) \
        -> dict[str, dict[str, int | float] | str]:
    return {
        "deviceMetrics": {
            "width": resolution[0],
            "height": resolution[1],
            "pixelRatio": 3.0,
        },
        "userAgent": user_agent
    }
