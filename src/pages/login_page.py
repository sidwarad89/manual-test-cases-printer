from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://qa-agent-platform.com"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    WELCOME_SPLASH_CLOSE = (By.CSS_SELECTOR, ".welcome-splash .close")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-inline")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, ".password-toggle")
    VALIDATION_ERROR = (By.CSS_SELECTOR, ".validation-error")

    def open(self):
        self.driver.get(self.URL)

    def dismiss_welcome(self):
        if self.is_displayed(self.WELCOME_SPLASH_CLOSE):
            self.click(self.WELCOME_SPLASH_CLOSE)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SIGNIN_BUTTON)

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text

    def get_validation_errors(self):
        return self.find_all(self.VALIDATION_ERROR)