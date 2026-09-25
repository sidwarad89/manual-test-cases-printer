from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="signup-username"]')
    EMAIL = (By.CSS_SELECTOR, '[data-testid="signup-email"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="signup-password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="signup-submit"]')
    RULE_LENGTH = (By.CSS_SELECTOR, '[data-testid="password-rule-length"]')
    RULE_UPPER = (By.CSS_SELECTOR, '[data-testid="password-rule-upper"]')
    RULE_NUMBER = (By.CSS_SELECTOR, '[data-testid="password-rule-number"]')
    RULE_SPECIAL = (By.CSS_SELECTOR, '[data-testid="password-rule-special"]')

    def open(self, base_url):
        self.driver.get(f"{base_url}/signup")

    def fill_form(self, username, email, password):
        self.type(self.USERNAME, username)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)

    def submit(self):
        self.click(self.SUBMIT)

    def get_rule_states(self):
        return {
            "length": self.is_visible(self.RULE_LENGTH),
            "upper": self.is_visible(self.RULE_UPPER),
            "number": self.is_visible(self.RULE_NUMBER),
            "special": self.is_visible(self.RULE_SPECIAL),
        }