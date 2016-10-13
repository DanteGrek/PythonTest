import pytest
import allure
from allure.constants import AttachmentType
from framework.driver_manager import Browser


@pytest.fixture(scope='class')
def setup_and_close_safari_on_ios(request):
    Browser.open_safari_on_ios()
    Browser.get_url('http://www.google.com')

    def close_browser():
        Browser.close_browser()
        print "request.fspath: ", request.fspath
    request.addfinalizer(close_browser)


@pytest.fixture(autouse=True)
def get_screenshot(request):

    def take_screenshot():
            allure.attach('screenshot', Browser.get_driver().get_screenshot_as_png(), type=AttachmentType.PNG)
    request.addfinalizer(take_screenshot)
