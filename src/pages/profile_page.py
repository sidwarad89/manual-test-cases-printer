from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = "[data-testid='feedback-text']"
    FEEDBACK_SUBMIT = "[data-testid='feedback-submit']"
    FEEDBACK_LIST = "[data-testid='feedback-list']"
    LOGOUT_BUTTON = "[data-testid='logout']"

    def open(self):
        self.driver.get(self.driver.current_url)  # Assuming already on profile URL

    def submit_feedback(self, message):
        self.type(By.CSS_SELECTOR, self.FEEDBACK_TEXT, message)
        self.click(By.CSS_SELECTOR, self.FEEDBACK_SUBMIT)

    def latest_feedback(self):
        feedback_items = self.driver.find_elements(By.CSS_SELECTOR, self.FEEDBACK_LIST + " > li")
        if feedback_items:
            return feedback_items[0].text
        return None

    def logout(self):
        self.click(By.CSS_SELECTOR, self.LOGOUT_BUTTON)