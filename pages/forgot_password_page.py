from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    # No explicit submit locator given; assuming pressing Enter works

    def open_forgot(self):
        self.click(self.FORGOT_LINK)

    def submit_email(self, email):
        self.type(self.EMAIL_FIELD, email)
        # Press Enter to submit
        self.find(self.EMAIL_FIELD).send_keys('\ue007')