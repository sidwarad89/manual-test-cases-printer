from selenium.webdriver.common.by import By

class HomePage:
    """Page Object for the example.com home page."""

    def __init__(self, driver):
        self.driver = driver
        self.heading_locator = (By.TAG_NAME, "h1")  # Example.com uses <h1>Example Domain</h1>

    def open(self):
        """Navigate to the base URL defined in config."""
        from src.config import BASE_URL
        self.driver.get(BASE_URL)

    def get_heading_text(self):
        """Return the text of the main heading."""
        element = self.driver.find_element(*self.heading_locator)
        return element.text