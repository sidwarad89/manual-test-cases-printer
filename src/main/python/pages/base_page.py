"""Base page object providing common utilities."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """All page objects should inherit from this class."""

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Wait for element to be present and return it."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            raise AssertionError(f"Element {locator} not found within timeout") from e

    def click(self, locator):
        """Wait for element to be clickable and click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text: str):
        """Clear a field and type text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url