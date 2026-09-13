from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    URL = "https://qa-agent-platform.com/forgot-password"

    EMAIL_INPUT = (By.ID, "forgot-email")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#forgot-submit")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, ".notification.success")

    def open(self):
        self.driver.get(self.URL)

    def recover(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def get_confirmation(self):
        return self.find(self.CONFIRM_MESSAGE).text