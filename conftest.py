import pytest


@pytest.fixture()
def web_driver_setup():
    print("Web driver init")

    yield

    print("Web driver close")
