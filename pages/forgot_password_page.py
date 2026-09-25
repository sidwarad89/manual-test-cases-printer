from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, '[data-testid="forgot-password-link"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="forgot-email"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="forgot-submit"]')  # Assuming a submit locator exists; if not, we will use the link click only.

    def click_forgot_link(self):
        self.click(self.FORGOT_LINK)

    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        # If a submit button is defined, click it; otherwise press Enter
        try:
            self.click(self.SUBMIT)
        except:
            self.driver.find_element(*self.EMAIL_INPUT).send_keys("\n")