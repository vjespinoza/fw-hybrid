import pytest
from appium import webdriver as awd
from selenium import webdriver as swd


@pytest.fixture()
def web_driver_setup() -> swd:
    print("Web driver init")

    yield

    print("Web driver close")


@pytest.fixture()
def app_driver_setup() -> awd:
    print("App driver init")

    yield

    print("App driver close")
