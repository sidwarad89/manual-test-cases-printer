from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="login-username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    ERROR = (By.CSS_SELECTOR, '[data-testid="login-error"]')
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, '[data-testid="login-password-toggle"]')
    # Optional splash close button (hypothetical)
    SPLASH_CLOSE = (By.CSS_SELECTOR, '[data-testid="welcome-splash-close"]')

    def dismiss_welcome_splash(self):
        if self.is_displayed(self.SPLASH_CLOSE):
            self.click(self.SPLASH_CLOSE)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_message(self):
        return self.get_text(self.ERROR)

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    def get_password_input_type(self):
        return self.get_attribute(self.PASSWORD, "type")