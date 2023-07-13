import pytest


@pytest.mark.usefixtures("setup")
class TestDummyWeb:
    def test_dummy_web_01(self) -> None:
        print('Dummy WEB test 01')
