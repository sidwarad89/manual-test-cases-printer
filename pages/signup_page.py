from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="signup-username"]')
    EMAIL = (By.CSS_SELECTOR, '[data-testid="signup-email"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="signup-password"]')
    PASSWORD_RULE_LENGTH = (By.CSS_SELECTOR, '[data-testid="password-rule-length"]')
    PASSWORD_RULE_UPPER = (By.CSS_SELECTOR, '[data-testid="password-rule-upper"]')
    PASSWORD_RULE_NUMBER = (By.CSS_SELECTOR, '[data-testid="password-rule-number"]')
    PASSWORD_RULE_SPECIAL = (By.CSS_SELECTOR, '[data-testid="password-rule-special"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="signup-submit"]')

    def load(self, url):
        self.driver.get(url)

    def fill_form(self, username, email, password):
        self.type(self.USERNAME, username)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)

    def submit(self):
        self.click(self.SUBMIT)

    def password_rule_is_visible(self, rule_locator):
        return self.is_displayed(rule_locator)