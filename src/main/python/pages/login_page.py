from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Page object representing the login screen."""

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON  = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username: str, password: str):
        """Perform login with provided credentials."""
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)