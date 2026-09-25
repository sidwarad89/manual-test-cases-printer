from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, '[data-testid="feedback-text"]')
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, '[data-testid="feedback-submit"]')
    FEEDBACK_LIST = (By.CSS_SELECTOR, '[data-testid="feedback-list"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-testid="logout"]')

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def get_latest_feedback(self):
        # Assuming the first item in the list represents the latest feedback
        first_item = self.find((By.CSS_SELECTOR, '[data-testid="feedback-list"] > *:first-child'))
        return first_item.text

    def logout(self):
        self.click(self.LOGOUT_BUTTON)