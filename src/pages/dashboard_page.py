"""Dashboard page object."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    LOGOUT_BUTTON = (By.ID, "logout")
    WELCOME_BANNER = (By.CSS_SELECTOR, ".welcome-banner")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        """Check that dashboard loaded by verifying welcome banner."""
        try:
            self.find(self.WELCOME_BANNER)
            return True
        except Exception:
            return False

    def logout(self):
        """Log out from the application."""
        self.click(self.LOGOUT_BUTTON)