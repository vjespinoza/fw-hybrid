import pytest


@pytest.mark.usefixtures("setup")
class TestDummyApp:
    def test_dummy_app_01(self) -> None:
        print('Dummy APP test 01')
