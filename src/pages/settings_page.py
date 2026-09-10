from selenium.webdriver.common.by import By
from .base_page import BasePage

class SettingsPage(BasePage):
    LOGOUT_BTN = (By.ID, "com.example.printerapp:id/btn_logout")

    def tap_logout(self):
        self.click(*self.LOGOUT_BTN)