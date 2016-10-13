from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.driver_manager import Browser
from framework.soft_assert import SoftAssert
from selenium.common.exceptions import TimeoutException
import locators.main_google_page_locators as locators
import allure


class AbstractPage(object):

    _CHANGE_TO_ENGLISH = (By.XPATH, "//a[text()='Change to English']", "Change to English")

    def __init__(self):
        self.driver = Browser.get_driver()

    def wait_for_element_to_be_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator=locator[:2]))
        except TimeoutException:
            return None

    def wait_for_elements(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(locator=locator[:2]))
        except TimeoutException:
            return None

    def wait_for_alert(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        except TimeoutException:
            return None

    @allure.step("Click on {1[2]}")
    def click(self, locator):
        self.wait_for_element_to_be_clickable(locator=locator).click()

    # @allure.step('Click on {2} from {1[2]}')
    def click_on_element_from_list(self, locator, index):
        self.wait_for_elements(locator).get(index).click()

    @allure.step("Input text: '{text}' into {1[2]}")
    def input_text(self, locator, text):
        element = self.wait_for_element_to_be_clickable(locator=locator)
        element.clear()
        element.send_keys(text)

    def select_english(self):
        if self.wait_for_element_to_be_clickable(self._CHANGE_TO_ENGLISH):
            self.click(self._CHANGE_TO_ENGLISH)


    def close_alert(self):
        if self.wait_for_alert():
            self.__close_alert()

    @allure.step("Close alert")
    def __close_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def accept_alert(self):
        if self.wait_for_alert():
            self.__accept_alert

    @allure.step("Accept alert")
    def __accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

class MainGooglePage(AbstractPage):

    def __init__(self):
        super(MainGooglePage, self).__init__()
        if Browser.driver_type is Browser.desktop:
            self.elements = locators.MainGooglePageDesktopLocators()
        elif Browser.driver_type is Browser.mobile:
            self.elements = locators.MainGooglePageMobileLocators()

    def search(self, text):
        self.input_text(self.elements.SEARCH_FIELD, text=text)
        self.click(self.elements.SUBMIT_BUTTON)
        self.close_alert()
        self.select_english()

    def is_search_result_contains(self, text):
        elements = self.wait_for_elements(self.elements.SEARCH_RESULTS)
        soft = SoftAssert()
        for element in elements:
            soft.assert_true(text in element.text, "'"+element.text+"' is not contains: '"+text+"'")
        soft.assert_all()
