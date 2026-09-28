from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="signup-username"]')
    EMAIL = (By.CSS_SELECTOR, '[data-testid="signup-email"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="signup-password"]')
    RULE_LENGTH = (By.CSS_SELECTOR, '[data-testid="password-rule-length"]')
    RULE_UPPER = (By.CSS_SELECTOR, '[data-testid="password-rule-upper"]')
    RULE_NUMBER = (By.CSS_SELECTOR, '[data-testid="password-rule-number"]')
    RULE_SPECIAL = (By.CSS_SELECTOR, '[data-testid="password-rule-special"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="signup-submit"]')

    def open(self, url):
        self.driver.get(url)

    def register(self, username, email, password):
        self.type(self.USERNAME, username)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_rule_status(self, rule_locator):
        element = self.find(rule_locator)
        # Assuming the rule element has a class indicating pass/fail; we just return its text
        return element.text