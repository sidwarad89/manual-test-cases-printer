from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, "[data-testid='feedback-text']")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, "[data-testid='feedback-submit']")
    FEEDBACK_LIST = (By.CSS_SELECTOR, "[data-testid='feedback-list']")  # Assuming a container

    def open(self, url):
        self.driver.get(url)

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def get_latest_feedback(self):
        # Returns the text of the first feedback item
        first_item = (self.FEEDBACK_LIST, 0)  # placeholder for demonstration
        # Simplify: assume each feedback entry has data-testid='feedback-item'
        items = self.driver.find_elements(By.CSS_SELECTOR, "[data-testid='feedback-item']")
        if items:
            return items[0].text
        return None