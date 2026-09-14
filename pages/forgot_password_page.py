from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, "[data-testid='forgot-password-link']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='forgot-email']")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid='login-submit']")  # Assuming same submit button

    def open(self, url):
        self.driver.get(url)

    def click_forgot_link(self):
        self.click(self.FORGOT_LINK)

    def reset_password(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT)