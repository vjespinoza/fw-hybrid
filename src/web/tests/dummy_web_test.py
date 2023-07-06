import pytest


@pytest.mark.usefixtures("web_driver_setup")
class TestDummyWeb:
    def test_dummy_web_01(self) -> None:
        pass
