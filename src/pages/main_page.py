from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # Locators (placeholders – replace with actual resource‑ids / accessibility ids)
    CONNECT_PRINTER_BTN = (By.ID, "com.example.pos:id/btn_connect_printer")
    PRINT_RECEIPT_BTN = (By.ID, "com.example.pos:id/btn_print_receipt")
    COMPLETE_SALE_BTN = (By.ID, "com.example.pos:id/btn_complete_sale")
    LOGOUT_BTN = (By.ID, "com.example.pos:id/btn_logout")
    NO_PRINTER_MSG = (By.ID, "com.example.pos:id/msg_no_printer")
    CONNECT_NOW_BTN = (By.ID, "com.example.pos:id/btn_connect_now")
    PRINTER_CONNECTED_INDICATOR = (By.ID, "com.example.pos:id/indicator_printer_connected")
    LOW_BATTERY_ICON = (By.ID, "com.example.pos:id/icon_low_battery")
    DUPLICATE_WATERMARK = (By.ID, "com.example.pos:id/watermark_duplicate")
    SUPERVISOR_PIN_INPUT = (By.ID, "com.example.pos:id/input_supervisor_pin")
    SUPERVISOR_SUBMIT_BTN = (By.ID, "com.example.pos:id/btn_submit_pin")
    PRINTER_ERROR_MSG = (By.ID, "com.example.pos:id/msg_printer_error")
    CONNECTION_LOST_MSG = (By.ID, "com.example.pos:id/msg_connection_lost")
    PRINTER_DISCONNECTED_MSG = (By.ID, "com.example.pos:id/msg_printer_disconnected")
    PRINTER_IN_USE_MSG = (By.ID, "com.example.pos:id/msg_printer_in_use")
    FIRMWARE_NOT_SUPPORTED_MSG = (By.ID, "com.example.pos:id/msg_firmware_not_supported")

    def tap_connect_printer(self):
        self.click(self.CONNECT_PRINTER_BTN)

    def tap_print_receipt(self):
        self.click(self.PRINT_RECEIPT_BTN)

    def tap_complete_sale(self):
        self.click(self.COMPLETE_SALE_BTN)

    def tap_logout(self):
        self.click(self.LOGOUT_BTN)

    def is_no_printer_message_displayed(self) -> bool:
        return self.is_displayed(self.NO_PRINTER_MSG)

    def tap_connect_now(self):
        self.click(self.CONNECT_NOW_BTN)

    def is_printer_connected(self) -> bool:
        return self.is_displayed(self.PRINTER_CONNECTED_INDICATOR)

    def get_connected_printer_name(self) -> str:
        # Assume the indicator also contains the printer name as its text
        return self.get_text(self.PRINTER_CONNECTED_INDICATOR)

    def is_low_battery_warning_displayed(self) -> bool:
        return self.is_displayed(self.LOW_BATTERY_ICON)

    def is_duplicate_watermark_displayed(self) -> bool:
        return self.is_displayed(self.DUPLICATE_WATERMARK)

    def enter_supervisor_pin(self, pin: str):
        self.send_keys(self.SUPERVISOR_PIN_INPUT, pin)
        self.click(self.SUPERVISOR_SUBMIT_BTN)

    def get_printer_error_message(self) -> str:
        return self.get_text(self.PRINTER_ERROR_MSG)

    def get_connection_lost_message(self) -> str:
        return self.get_text(self.CONNECTION_LOST_MSG)

    def get_printer_disconnected_message(self) -> str:
        return self.get_text(self.PRINTER_DISCONNECTED_MSG)

    def get_printer_in_use_message(self) -> str:
        return self.get_text(self.PRINTER_IN_USE_MSG)

    def get_firmware_not_supported_message(self) -> str:
        return self.get_text(self.FIRMWARE_NOT_SUPPORTED_MSG)