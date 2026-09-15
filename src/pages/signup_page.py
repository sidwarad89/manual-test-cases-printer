from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid=signup-username]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid=signup-email]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid=signup-password]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid=signup-submit]")
    RULE_LENGTH = (By.CSS_SELECTOR, "[data-testid=password-rule-length]")
    RULE_UPPER = (By.CSS_SELECTOR, "[data-testid=password-rule-upper]")
    RULE_NUMBER = (By.CSS_SELECTOR, "[data-testid=password-rule-number]")
    RULE_SPECIAL = (By.CSS_SELECTOR, "[data-testid=password-rule-special]")

    def open(self, base_url):
        self.driver.get(f"{base_url}/signup")

    def sign_up(self, username, email, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_rule_status(self, rule_locator):
        elem = self.wait_for_element(rule_locator)
        return elem.get_attribute("class")  # assumes a class indicates pass/fail

    def get_all_rules_status(self):
        return {
            "length": self.get_rule_status(self.RULE_LENGTH),
            "upper": self.get_rule_status(self.RULE_UPPER),
            "number": self.get_rule_status(self.RULE_NUMBER),
            "special": self.get_rule_status(self.RULE_SPECIAL),
        }