from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    CONNECT_PRINTER_BTN = (By.ID, "com.example.printerapp:id/btn_connect_printer")
    PRINT_RECEIPT_BTN = (By.ID, "com.example.printerapp:id/btn_print_receipt")
    LOGOUT_BTN = (By.ID, "com.example.printerapp:id/btn_logout")
    SETTINGS_BTN = (By.ID, "com.example.printerapp:id/btn_settings")
    PRINTER_STATUS = (By.ID, "com.example.printerapp:id/tv_printer_status")
    LOW_BATTERY_ICON = (By.ID, "com.example.printerapp:id/iv_low_battery")

    def tap_connect_printer(self):
        self.click(*self.CONNECT_PRINTER_BTN)

    def tap_print_receipt(self):
        self.click(*self.PRINT_RECEIPT_BTN)

    def tap_logout(self):
        self.click(*self.LOGOUT_BTN)

    def get_printer_status(self):
        return self.get_text(*self.PRINTER_STATUS)

    def is_low_battery_icon_displayed(self):
        return self.is_displayed(*self.LOW_BATTERY_ICON)