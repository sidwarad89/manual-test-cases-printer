from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="forgot-submit"]')
    CONFIRMATION = (By.CSS_SELECTOR, '[data-testid="forgot-confirmation"]')

    def open_forgot_form(self):
        self.click(self.FORGOT_LINK)

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT)

    def confirmation_is_displayed(self):
        return self.is_displayed(self.CONFIRMATION)