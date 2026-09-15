from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid=forgot-email]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid=login-submit]")  # Re‑using submit btn on the same page
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, "[data-testid=forgot-confirm]")  # assumed locator

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def get_confirmation(self):
        return self.get_text(self.CONFIRM_MESSAGE)