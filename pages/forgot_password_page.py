from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, "[data-testid=forgot-password-link]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid=forgot-email]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid=forgot-submit]")  # Assuming a submit button with this ID
    CONFIRMATION = (By.CSS_SELECTOR, "[data-testid=forgot-confirmation]")

    def open_forgot(self):
        self.click(self.FORGOT_LINK)

    def reset(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def confirmation_visible(self):
        return self.is_displayed(self.CONFIRMATION)