from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="forgot-submit"]')
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, '[data-testid="forgot-confirm"]')

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def confirmation_displayed(self):
        return self.is_displayed(self.CONFIRM_MESSAGE)