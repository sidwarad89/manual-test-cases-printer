from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid=login-username]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid=login-password]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid=login-submit]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid=login-error]")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "[data-testid=login-password-toggle]")
    FORGOT_LINK = (By.CSS_SELECTOR, "[data-testid=forgot-password-link]")

    def open(self, base_url):
        self.driver.get(base_url)

    def dismiss_welcome_splash(self):
        # Attempt to close a possible welcome splash; ignore if not present
        try:
            splash_close = (By.CSS_SELECTOR, "[data-testid=welcome-splash-close]")
            self.click(splash_close)
        except Exception:
            pass

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error(self):
        return self.get_text(self.ERROR_MESSAGE)

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    def get_password_field_type(self):
        elem = self.wait_for_element(self.PASSWORD_INPUT)
        return elem.get_attribute("type")

    def click_forgot_password(self):
        self.click(self.FORGOT_LINK)