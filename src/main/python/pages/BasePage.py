import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    All page objects should inherit from this class.
    It provides common utilities like waiting for elements.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.logger = logging.getLogger(self.__class__.__name__)

    def find(self, locator):
        """Wait for visibility and return the WebElement."""
        self.logger.debug(f"Waiting for element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        elem = self.find(locator)
        elem.click()
        self.logger.debug(f"Clicked element: {locator}")

    def send_keys(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)
        self.logger.debug(f"Sent keys to {locator}: {text}")