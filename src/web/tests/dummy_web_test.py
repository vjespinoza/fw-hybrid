import pytest


@pytest.mark.usefixtures("set_up")
class TestDummyWeb:
    def test_dummy_web_01(self) -> None:
        print('Dummy web test 01')
