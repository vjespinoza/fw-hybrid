from typing import Tuple, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from config.driver.driver import get_driver
from config.local_environment import LocalEnvironment


@pytest.fixture()
def execution_details() -> Tuple[str, str, bool, bool]:
    """
    Instantiates the local environment class and returns execution details
    :return: tuple with environment variables
    """
    print("Reading env variables")
    local_env = LocalEnvironment()
    name = local_env.get_platform_name()
    size = local_env.get_scren_size()
    is_web = local_env.is_web()
    is_local = local_env.is_local()

    return name, size, is_web, is_local


@pytest.fixture()
def set_up(
        execution_details: Tuple[str, str, bool, bool]
) -> Generator[WebDriver, None, None]:
    """
    Preforms driver set up and teardown
    :param execution_details: values obtained from the local environment
    :return: driver instance
    """
    print("Using driver fixture - START")
    driver = get_driver(*execution_details)
    driver.get('https://youtube.com/')
    yield driver
    driver.close()
    print("Using driver fixture - END")
