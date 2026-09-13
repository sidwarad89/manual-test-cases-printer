from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_MENU = (By.CSS_SELECTOR, "[data-testid='nav-profile']")  # assumed
    LOGOUT_BTN = (By.CSS_SELECTOR, "[data-testid='logout']")
    FEEDBACK_TEXT = (By.CSS_SELECTOR, "[data-testid='feedback-text']")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, "[data-testid='feedback-submit']")
    FEEDBACK_LIST = (By.CSS_SELECTOR, "[data-testid='feedback-list']")  # assumed

    def open(self):
        # assume profile page reachable via nav-profile click
        self.click(self.PROFILE_MENU)

    def submit_feedback(self, message):
        self.type(self.FEEDBACK_TEXT, message)
        self.click(self.FEEDBACK_SUBMIT)

    def get_latest_feedback(self):
        return self.find(self.FEEDBACK_LIST).text

    def logout(self):
        self.click(self.LOGOUT_BTN)