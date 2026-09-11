from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="signup-username"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="signup-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="signup-password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="signup-submit"]')
    RULE_LENGTH = (By.CSS_SELECTOR, '[data-testid="password-rule-length"]')
    RULE_UPPER = (By.CSS_SELECTOR, '[data-testid="password-rule-upper"]')
    RULE_NUMBER = (By.CSS_SELECTOR, '[data-testid="password-rule-number"]')
    RULE_SPECIAL = (By.CSS_SELECTOR, '[data-testid="password-rule-special"]')

    def open(self, url):
        self.driver.get(url)

    def sign_up(self, username, email, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def password_rule_failed(self, rule_locator):
        return self.is_displayed(rule_locator)