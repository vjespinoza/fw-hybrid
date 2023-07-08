from typing import Tuple, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from config.driver import get_web_driver


@pytest.fixture()
def execution_params() -> Tuple[str, bool]:
    """
    Reads local environment and returns execution configuration variables
    :return: tuple with environment variables
    """
    print("Reading env variables")
    return "firefox", True


@pytest.fixture()
def set_up(execution_params: Tuple[str, bool]) -> Generator[WebDriver, None, None]:
    """
    Preforms driver set up and teardown
    :param execution_params: values obtained from the local environment
    :return: driver instance
    """
    print("Using driver fixture - STAR")
    driver = get_web_driver(*execution_params)
    driver.get('https://youtube.com/')
    yield driver
    driver.close()
    print("Using driver fixture - END")
