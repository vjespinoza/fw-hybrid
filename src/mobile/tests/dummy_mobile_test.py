import pytest


@pytest.mark.usefixtures("app_driver_setup")
class TestDummyApp:
    def test_dummy_app_01(self) -> None:
        pass
