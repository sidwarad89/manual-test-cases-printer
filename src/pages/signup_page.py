from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class SignUpPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-testid=signup-username]")
    EMAIL = (By.CSS_SELECTOR, "[data-testid=signup-email]")
    PASSWORD = (By.CSS_SELECTOR, "[data-testid=signup-password]")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid=signup-submit]")
    RULE_LENGTH = (By.CSS_SELECTOR, "[data-testid=password-rule-length]")
    RULE_UPPER = (By.CSS_SELECTOR, "[data-testid=password-rule-upper]")
    RULE_NUMBER = (By.CSS_SELECTOR, "[data-testid=password-rule-number]")
    RULE_SPECIAL = (By.CSS_SELECTOR, "[data-testid=password-rule-special]")

    def sign_up(self, username, email, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_unmet_rules(self):
        rules = []
        for name, locator in [
            ("length", self.RULE_LENGTH),
            ("upper", self.RULE_UPPER),
            ("number", self.RULE_NUMBER),
            ("special", self.RULE_SPECIAL),
        ]:
            if self.is_visible(locator):
                rules.append(name)
        return rules