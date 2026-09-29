from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-testid=login-username]")
    PASSWORD = (By.CSS_SELECTOR, "[data-testid=login-password]")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid=login-submit]")
    ERROR = (By.CSS_SELECTOR, "[data-testid=login-error]")
    WELCOME_CLOSE = (By.CSS_SELECTOR, "[data-testid=welcome-close]")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "[data-testid=login-password-toggle]")

    def dismiss_welcome_if_present(self):
        if self.is_visible(self.WELCOME_CLOSE):
            self.click(self.WELCOME_CLOSE)

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_text(self):
        if self.is_visible(self.ERROR):
            return self.find(self.ERROR).text
        return ""

    def toggle_password_visibility(self):
        if self.is_visible(self.PASSWORD_TOGGLE):
            self.click(self.PASSWORD_TOGGLE)

    def password_field_type(self):
        return self.get_attribute(self.PASSWORD, "type")