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

    def load(self, url):
        self.driver.get(url)

    def sign_up(self, username, email, password):
        self.type(self.USERNAME, username)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def are_password_rules_visible(self):
        return all([
            self.is_displayed(self.RULE_LENGTH),
            self.is_displayed(self.RULE_UPPER),
            self.is_displayed(self.RULE_NUMBER),
            self.is_displayed(self.RULE_SPECIAL)
        ])