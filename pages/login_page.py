from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="login-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-testid="login-error"]')
    FORGOT_LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, '[data-testid="login-password-toggle"]')

    def open(self, url):
        self.driver.get(url)

    def dismiss_welcome(self):
        # If a splash exists it might have a known test-id; ignore if not present
        pass

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def login_error_present(self):
        return self.is_displayed(self.ERROR_MESSAGE)

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    def password_field_type(self):
        return self.get_attribute(self.PASSWORD_INPUT, "type")