from selenium import webdriver as SWD
from appium import webdriver as AWD


class Browser:

    driver = None
    driver_type = "default"
    desktop = "desktop"
    mobile = "mobile"

    @classmethod
    def get_driver(cls):
        if cls.driver:
            return cls.driver

    @classmethod
    def open_local_chrome(cls):
        cls.driver = SWD.Chrome()
        cls.driver.maximize_window()
        cls.driver_type = cls.desktop

    @classmethod
    def open_safari_on_ios(cls):
        cap = {
            'newCommandTimeout': 0,
            'platformVersion': '9.3',
            # 'automationName': 'XCUITest',
            'platformName': 'iOS',
            'browserName': 'Safari',
            'deviceName': 'iPhone 6s'}
        cls.driver = AWD.Remote('http://localhost:4723/wd/hub', cap)
        cls.driver_type = cls.mobile
        return cls.driver

    @classmethod
    def get_url(cls, url):
        cls.driver.get(url=url)

    @classmethod
    def close_browser(cls):
        cls.driver.quit()

if __name__ == '__main__':
    Browser.open_local_chrome()

    fails = []

    try:
        assert Browser.driver_type is Browser.mobile, "message"
    except AssertionError:
        print "@"
    finally:
        pass
    Browser.close_browser()