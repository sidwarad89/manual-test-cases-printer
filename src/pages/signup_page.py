from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class SignUpPage(BasePage):
    USERNAME = "[data-testid='signup-username']"
    EMAIL = "[data-testid='signup-email']"
    PASSWORD = "[data-testid='signup-password']"
    SUBMIT = "[data-testid='signup-submit']"

    RULE_LENGTH = "[data-testid='password-rule-length']"
    RULE_UPPER = "[data-testid='password-rule-upper']"
    RULE_NUMBER = "[data-testid='password-rule-number']"
    RULE_SPECIAL = "[data-testid='password-rule-special']"

    def open(self, url):
        self.driver.get(url)

    def fill_form(self, username, email, password):
        self.type(By.CSS_SELECTOR, self.USERNAME, username)
        self.type(By.CSS_SELECTOR, self.EMAIL, email)
        self.type(By.CSS_SELECTOR, self.PASSWORD, password)

    def submit(self):
        self.click(By.CSS_SELECTOR, self.SUBMIT)

    def get_unmet_rules(self):
        rules = {}
        for name, locator in [
            ("length", self.RULE_LENGTH),
            ("upper", self.RULE_UPPER),
            ("number", self.RULE_NUMBER),
            ("special", self.RULE_SPECIAL),
        ]:
            rules[name] = self.is_displayed(By.CSS_SELECTOR, locator)
        return rules