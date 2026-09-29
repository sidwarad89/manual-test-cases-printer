from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    LINK = (By.CSS_SELECTOR, "[data-testid=forgot-password-link]")
    EMAIL = (By.CSS_SELECTOR, "[data-testid=forgot-email]")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid=login-submit]")  # Assuming same submit button
    CONFIRMATION = (By.CSS_SELECTOR, "[data-testid=forgot-confirmation]")

    def open_forgot_form(self):
        self.click(self.LINK)

    def submit_email(self, email):
        self.send_keys(self.EMAIL, email)
        self.click(self.SUBMIT)

    def is_confirmation_visible(self):
        return self.is_visible(self.CONFIRMATION)