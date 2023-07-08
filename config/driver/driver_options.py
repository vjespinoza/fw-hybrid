from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import ArgOptions


# from selenium.webdriver.firefox.options import Options as FirefoxOptions


def _set_remote_options(options: ArgOptions) -> None:
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    options.set_capability("sauce:options", "Implement helper func")


def chrome_options(is_local: bool = True) -> ArgOptions:
    opts = ChromeOptions()
    if is_local:
        opts.add_experimental_option("mobileEmulation", "implement helper func")
    else:
        _set_remote_options(options=opts)
    return opts
