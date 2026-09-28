from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    EMAIL = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="forgot-submit"]')  # Not listed; assume same as login-submit if needed

    def click_forgot_link(self):
        self.click(self.LINK)

    def submit_email(self, email):
        self.type(self.EMAIL, email)
        # Assuming the same submit button as login-submit exists on the forgot password form
        self.click((By.CSS_SELECTOR, '[data-testid="login-submit"]'))

    def is_email_field_cleared(self):
        element = self.find(self.EMAIL)
        return element.get_attribute("value") == ""