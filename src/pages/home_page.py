from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """Home page of the POS application."""

    CONNECT_PRINTER_BTN = (By.ID, "connect_printer_btn")
    PRINT_RECEIPT_BTN = (By.ID, "print_receipt_btn")
    SETTINGS_BTN = (By.ID, "settings_btn")

    def open(self, url="http://localhost:8080"):
        self.driver.get(url)

    def tap_connect_printer(self):
        self.click(self.CONNECT_PRINTER_BTN)

    def tap_print_receipt(self):
        self.click(self.PRINT_RECEIPT_BTN)

    def tap_settings(self):
        self.click(self.SETTINGS_BTN)