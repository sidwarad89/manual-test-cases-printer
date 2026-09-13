from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, '[data-testid="feedback-text"]')
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, '[data-testid="feedback-submit"]')
    FEEDBACK_LIST = (By.CSS_SELECTOR, '[data-testid="feedback-list"]')  # hypothetical
    FEEDBACK_ITEM = (By.CSS_SELECTOR, '[data-testid="feedback-item"]')  # first item

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def latest_feedback_text(self):
        return self.get_text(self.FEEDBACK_ITEM)