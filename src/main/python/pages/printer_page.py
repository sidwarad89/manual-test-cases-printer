from selenium.webdriver.common.by import By
from .base_page import BasePage


class PrinterPage(BasePage):
    # Locators (placeholders – replace with real resource‑ids / xpath)
    CONNECT_PRINTER_BTN = (By.ID, "com.example.posapp:id/btn_connect_printer")
    PRINTER_LIST = (By.ID, "com.example.posapp:id/printer_list")
    PRINTER_ITEM = (By.XPATH, "//android.widget.TextView[@text='{printer_name}']")
    CONNECTED_INDICATOR = (By.ID, "com.example.posapp:id/printer_connected")
    PRINT_RECEIPT_BTN = (By.ID, "com.example.posapp:id/btn_print_receipt")
    STATUS_MESSAGE = (By.ID, "com.example.posapp:id/status_message")
    RECONNECT_BTN = (By.ID, "com.example.posapp:id/btn_reconnect")
    DUPLICATE_WATERMARK = (By.ID, "com.example.posapp:id/watermark_duplicate")
    SUPERVISOR_PIN_FIELD = (By.ID, "com.example.posapp:id/pin_input")
    SUPERVISOR_PIN_OK = (By.ID, "com.example.posapp:id/pin_ok")
    LOW_BATTERY_ICON = (By.ID, "com.example.posapp:id/icon_low_battery")
    LOGOUT_BTN = (By.ID, "com.example.posapp:id/btn_logout")

    def open_printer_connection(self):
        self.click(self.CONNECT_PRINTER_BTN)

    def wait_for_printer_list(self):
        return self.is_displayed(self.PRINTER_LIST)

    def select_printer(self, printer_name):
        locator = (self.PRINTER_ITEM[0],
                   self.PRINTER_ITEM[1].format(printer_name=printer_name))
        self.click(locator)

    def get_connected_printer_name(self):
        return self.get_text(self.CONNECTED_INDICATOR)

    def tap_print_receipt(self):
        self.click(self.PRINT_RECEIPT_BTN)

    def get_status_message(self):
        return self.get_text(self.STATUS_MESSAGE)

    def tap_reconnect(self):
        self.click(self.RECONNECT_BTN)

    def is_duplicate_watermark_displayed(self):
        return self.is_displayed(self.DUPLICATE_WATERMARK)

    def enter_supervisor_pin(self, pin):
        self.send_keys(self.SUPERVISOR_PIN_FIELD, pin)
        self.click(self.SUPERVISOR_PIN_OK)

    def is_low_battery_icon_visible(self):
        return self.is_displayed(self.LOW_BATTERY_ICON)

    def logout(self):
        self.click(self.LOGOUT_BTN)