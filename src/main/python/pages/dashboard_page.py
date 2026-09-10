"""Dashboard page object model."""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    LOGOUT_BUTTON = (By.ID, "logout")
    WELCOME_BANNER = (By.CSS_SELECTOR, ".welcome")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Simple check that dashboard loaded by verifying the welcome banner."""
        try:
            self.find(self.WELCOME_BANNER)
            return True
        except AssertionError:
            return False

    def logout(self):
        self.click(self.LOGOUT_BUTTON)