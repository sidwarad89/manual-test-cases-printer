from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_INPUT = (By.CSS_SELECTOR, "[data-testid=feedback-text]")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, "[data-testid=feedback-submit]")
    FEEDBACK_LIST = (By.CSS_SELECTOR, "[data-testid=feedback-list]")  # Assuming a container
    FEEDBACK_ITEMS = (By.CSS_SELECTOR, "[data-testid=feedback-item]")  # Individual items

    def open(self):
        # Assuming there is a direct URL or a sidebar link; we'll navigate directly
        self.driver.get(f"{self.driver.current_url.rstrip('/')}/profile")

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_INPUT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def feedback_contains(self, message):
        items = self.driver.find_elements(*self.FEEDBACK_ITEMS)
        return any(message in item.text for item in items)