"""Login page object."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username: str, password: str):
        """Perform login with supplied credentials."""
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        """Return error text if login fails."""
        try:
            return self.find(self.ERROR_MESSAGE).text
        except Exception:
            return None