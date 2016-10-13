from framework.driver_manager import Browser
import pytest


@pytest.fixture(scope="class")
def start_and_close_desktop_chrome(request):
    Browser.open_local_chrome()
    Browser.get_url("http://www.google.com")

    def close_chrome():
        Browser.close_browser()
    request.addfinalizer(close_chrome)
