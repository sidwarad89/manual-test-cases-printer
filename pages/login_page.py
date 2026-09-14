from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-testid='login-username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-testid='login-password']")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid='login-submit']")
    ERROR = (By.CSS_SELECTOR, "[data-testid='login-error']")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, "[data-testid='login-password-toggle']")
    WELCOME_DISMISS = (By.CSS_SELECTOR, "[data-testid='welcome-dismiss']")

    def open(self, url):
        self.driver.get(url)

    def dismiss_welcome(self):
        if self.is_displayed(self.WELCOME_DISMISS):
            self.click(self.WELCOME_DISMISS)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_message(self):
        return self.find(self.ERROR).text

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    def password_field_type(self):
        return self.get_attribute(self.PASSWORD, "type")