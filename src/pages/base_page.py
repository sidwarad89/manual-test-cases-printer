from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class that all page objects inherit from."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """Find element using a locator tuple (By, value)."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click on element located by locator."""
        self.find(locator).click()

    def send_keys(self, locator, text):
        """Send text to element located by locator."""
        self.find(locator).clear()
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        """Return True if element is visible."""
        try:
            return self.find(locator).is_displayed()
        except:
            return False