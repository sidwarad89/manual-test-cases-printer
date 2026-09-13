from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    URL = "https://qa-agent-platform.com/signup"

    USERNAME_INPUT = (By.ID, "signup-username")
    EMAIL_INPUT = (By.ID, "signup-email")
    PASSWORD_INPUT = (By.ID, "signup-password")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button#signup")
    PASSWORD_UNMET_RULE = (By.CSS_SELECTOR, ".pwd-strength .unmet")

    def open(self):
        self.driver.get(self.URL)

    def sign_up(self, username, email, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BUTTON)

    def unmet_strength_rules(self):
        elems = self.find_all(self.PASSWORD_UNMET_RULE)
        return [e.text for e in elems]