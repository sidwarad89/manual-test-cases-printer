import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects, providing common utilities."""
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def find(self, locator):
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click on the element identified by the locator."""
        element = self.find(locator)
        element.click()

    def type(self, locator, text):
        """Send text to the element identified by the locator."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def pause(self, seconds=1):
        """Utility pause – use sparingly (mainly for debugging)."""
        time.sleep(seconds)