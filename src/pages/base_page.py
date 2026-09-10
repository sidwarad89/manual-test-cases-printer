from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class for all page objects. Provides common Selenium/Appium utilities.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()
        return element

    def send_keys(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)
        return element

    def is_displayed(self, by, locator):
        try:
            return self.find(by, locator).is_displayed()
        except:
            return False

    def get_text(self, by, locator):
        return self.find(by, locator).text