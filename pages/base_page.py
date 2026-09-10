```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """All page objects inherit from this class."""

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.timeout = 10  # seconds

    def find(self, locator):
        """Find element with explicit wait."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            self.logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element NOT found within {self.timeout}s: {locator}")
            raise

    def click(self, locator):
        """Click element after waiting for it to be clickable."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        self.logger.debug(f"Clicked element: {locator}")

    def type(self, locator, text):
        """Clear the field and type given text."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        self.logger.debug(f"Typed '{text}' into element: {locator}")

    def get_title(self):
        """Return the current page title."""
        title = self.driver.title
        self.logger.debug(f"Current page title: {title}")
        return title

    def get_url(self):
        """Return the current URL."""
        url = self.driver.current_url
        self.logger.debug(f"Current URL: {url}")
        return url

    def is_displayed(self, locator) -> bool:
        """Return True if element is visible."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.debug(f"Element is visible: {locator}")
            return element.is_displayed()
        except TimeoutException:
            self.logger.debug(f"Element not visible after {self.timeout}s: {locator}")
            return False
```

---  