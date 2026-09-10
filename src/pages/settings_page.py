from selenium.webdriver.common.by import By
from .base_page import BasePage

class SettingsPage(BasePage):
    """Settings and logout page."""

    LOGOUT_BTN = (By.ID, "logout_btn")

    def logout(self):
        self.click(self.LOGOUT_BTN)