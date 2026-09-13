from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class SignupPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid='signup-username']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='signup-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='signup-password']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid='signup-submit']")

    # Password rule locators
    RULE_LENGTH = (By.CSS_SELECTOR, "[data-testid='password-rule-length']")
    RULE_UPPER = (By.CSS_SELECTOR, "[data-testid='password-rule-upper']")
    RULE_NUMBER = (By.CSS_SELECTOR, "[data-testid='password-rule-number']")
    RULE_SPECIAL = (By.CSS_SELECTOR, "[data-testid='password-rule-special']")

    def open(self):
        from src.config import BASE_URL
        self.driver.get(f"{BASE_URL}/signup")

    def signup(self, username, email, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    def password_rules(self):
        return {
            "length": self.is_displayed(self.RULE_LENGTH),
            "upper": self.is_displayed(self.RULE_UPPER),
            "number": self.is_displayed(self.RULE_NUMBER),
            "special": self.is_displayed(self.RULE_SPECIAL)
        }