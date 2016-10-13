from selenium.webdriver.common.by import By


class MainGooglePageDesktopLocators:

    SEARCH_FIELD = (By.XPATH, "//input[@type='text' and @name]", "Input field")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']", "Submit button")
    SEARCH_RESULTS = (By.XPATH, "//h3/a", "Search result")


class MainGooglePageMobileLocators:

    SEARCH_FIELD = (By.XPATH, "//input[@class]", "Input field")
    SUBMIT_BUTTON = (By.XPATH, "//button", "Submit button")
    SEARCH_RESULTS = (By.XPATH, "//h3/a", "Search result")