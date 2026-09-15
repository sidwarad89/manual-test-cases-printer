from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_INPUT = (By.CSS_SELECTOR, "[data-testid=feedback-text]")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, "[data-testid=feedback-submit]")
    FEEDBACK_LIST = (By.CSS_SELECTOR, "[data-testid=feedback-list]")  # container for entries

    def open_via_sidebar(self, sidebar):
        # Assuming there is a nav item for profile; using logout element as placeholder
        # Real locator should be provided – using logout for demo purposes
        pass

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_INPUT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def get_latest_feedback(self):
        # Returns text of the most recent feedback entry
        entries = self.wait.until(EC.presence_of_all_elements_located(self.FEEDBACK_LIST))
        if entries:
            return entries[0].text
        return ""