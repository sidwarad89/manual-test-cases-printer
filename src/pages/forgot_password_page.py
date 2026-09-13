from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, "[data-testid='forgot-password-link']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='forgot-email']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid='forgot-submit']")  # assuming same as login-submit if not defined

    def click_forgot(self):
        self.click(self.FORGOT_LINK)

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BTN)