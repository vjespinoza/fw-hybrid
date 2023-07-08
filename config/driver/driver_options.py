from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.driver.driver_helper import set_mobile_emulation, set_remote_options


def chrome_options(is_local: bool = True) -> BaseOptions:
    opts = ChromeOptions()
    ua = "Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RD1A.201105.003.C1; wv)" \
         " AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66" \
         " Mobile Safari/537.36"
    if is_local:
        opts.add_experimental_option("mobileEmulation",
                                     set_mobile_emulation((393, 851), ua))
    else:
        set_remote_options(options=opts)
    return opts


def firefox_options(is_local: bool = True) -> BaseOptions:
    opts = FirefoxOptions()
    ua = "Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RD1A.201105.003.C1; wv)" \
         " AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66" \
         " Mobile Safari/537.36"
    if is_local:
        opts.set_preference("general.useragent.override", ua)
        opts.add_argument(argument="--width=393")
        opts.add_argument(argument="--height=851")
    else:
        set_remote_options(options=opts)
    return opts
