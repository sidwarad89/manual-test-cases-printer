from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = "[data-testid='forgot-email']"
    SUBMIT = "[data-testid='forgot-submit']"
    CONFIRM_MSG = "[data-testid='forgot-confirm']"

    def submit_email(self, email):
        self.type(By.CSS_SELECTOR, self.EMAIL_INPUT, email)
        self.click(By.CSS_SELECTOR, self.SUBMIT)

    def get_confirmation(self):
        return self.get_text(By.CSS_SELECTOR, self.CONFIRM_MSG)