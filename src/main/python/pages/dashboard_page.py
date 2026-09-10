from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    """Page object representing the dashboard after a successful login."""

    # Example locator – adjust to the actual application
    WELCOME_BANNER = (By.ID, "welcome-banner")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Return True if the dashboard appears to be fully loaded."""
        try:
            self.find(self.WELCOME_BANNER)
            return True
        except Exception:
            return False