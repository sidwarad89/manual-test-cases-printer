from selenium.webdriver.common.by import By
from typing import Tuple
from pages.base_page import BasePage

class PrinterPage(BasePage):
    """Page object for the Printer screen of the Android app."""

    # Example locators – adjust to the real app's UI IDs
    PRINT_BUTTON: Tuple[By, str] = (By.ID, "com.example.printer:id/btn_print")
    STATUS_LABEL: Tuple[By, str] = (By.ID, "com.example.printer:id/tv_status")
    DOCUMENT_FIELD: Tuple[By, str] = (By.ID, "com.example.printer:id/et_document")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_document_name(self, name: str):
        self.send_keys(self.DOCUMENT_FIELD, name)

    def tap_print(self):
        self.click(self.PRINT_BUTTON)

    def get_status(self) -> str:
        return self.get_text(self.STATUS_LABEL)