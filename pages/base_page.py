from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def find(self, locator):
        """Locate a single element."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def finds(self, locator):
        """Locate multiple elements."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        elem = self.find(locator)
        elem.click()

    def send_keys(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_visibility(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )