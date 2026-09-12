from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid=login-username]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid=login-password]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid=login-submit]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid=login-error]")
    WELCOME_SPLASH = (By.CSS_SELECTOR, "[data-testid=welcome-splash]")
    WELCOME_DISMISS = (By.CSS_SELECTOR, "[data-testid=welcome-dismiss]")

    def open(self):
        self.driver.get(BASE_URL)

    def dismiss_welcome(self):
        if self.is_displayed(self.WELCOME_SPLASH):
            self.click(self.WELCOME_DISMISS)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_error(self):
        return self.get_text(self.ERROR_MESSAGE) if self.is_displayed(self.ERROR_MESSAGE) else None

    def password_input_type(self):
        return self.get_attribute(self.PASSWORD_INPUT, "type")

    def toggle_password_visibility(self):
        TOGGLE = (By.CSS_SELECTOR, "[data-testid=login-password-toggle]")
        self.click(TOGGLE)