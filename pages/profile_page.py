from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, '[data-testid="feedback-text"]')
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, '[data-testid="feedback-submit"]')
    FEEDBACK_LIST = (By.CSS_SELECTOR, '[data-testid="feedback-list"]')
    # Assuming each feedback entry has a data-testid like "feedback-item-<index>"
    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def feedback_appears(self, message):
        # Simplistic check: look for the exact text somewhere in the list
        self.wait.until(EC.visibility_of_element_located(self.FEEDBACK_LIST))
        return message in self.driver.page_source