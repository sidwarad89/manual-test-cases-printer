from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, '[data-testid="feedback-text"]')
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, '[data-testid="feedback-submit"]')

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def is_feedback_field_cleared(self):
        element = self.find(self.FEEDBACK_TEXT)
        return element.get_attribute("value") == ""