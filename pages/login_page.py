from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="login-username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    ERROR = (By.CSS_SELECTOR, '[data-testid="login-error"]')
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, '[data-testid="login-password-toggle"]')

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def login_with_invalid_password(self, username, wrong_password):
        self.login(username, wrong_password)

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    def get_password_input_type(self):
        return self.get_attribute(self.PASSWORD, "type")