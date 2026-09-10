"""Base Page class containing common Selenium actions."""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """All page objects should inherit from this class."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator):
        """Wait for element to be present and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """Click on an element located by the given locator."""
        element = self.find(locator)
        element.click()

    def type(self, locator, text):
        """Clear the field and type the given text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title