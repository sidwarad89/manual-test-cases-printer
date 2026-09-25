from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="forgot-submit"]')
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, '[data-testid="forgot-confirm"]')

    def open(self, base_url):
        self.driver.get(base_url)

    def click_forgot_link(self):
        self.click(self.LINK)

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT)

    def get_confirmation(self):
        return self.get_text(self.CONFIRM_MESSAGE)