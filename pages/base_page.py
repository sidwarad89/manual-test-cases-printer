from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    def get_text(self, locator):
        element = self.find(locator)
        return element.text