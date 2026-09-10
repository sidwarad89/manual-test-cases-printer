from selenium.webdriver.common.by import By
from .base_page import BasePage

class PrintReceiptPage(BasePage):
    """Page handling receipt printing."""

    STATUS_LABEL = (By.ID, "print_status")
    DUPLICATE_WATERMARK = (By.ID, "duplicate_watermark")
    ERROR_MSG = (By.ID, "error_message")
    RETRY_BTN = (By.ID, "retry_btn")
    CONNECT_NOW_BTN = (By.ID, "connect_now_btn")
    LOW_BATTERY_ICON = (By.ID, "low_battery_icon")
    SUPERVISOR_PIN_INPUT = (By.ID, "supervisor_pin")
    CONFIRM_PIN_BTN = (By.ID, "confirm_pin_btn")

    def start_print(self):
        """Assumes the Print Receipt button has already been tapped on HomePage."""
        # In a real app the print starts automatically after tapping.
        pass

    def get_status_text(self):
        return self.find(self.STATUS_LABEL).text

    def is_duplicate_watermark_present(self):
        return self.is_displayed(self.DUPLICATE_WATERMARK)

    def get_error_message(self):
        return self.find(self.ERROR_MSG).text if self.is_displayed(self.ERROR_MSG) else ""

    def tap_retry(self):
        self.click(self.RETRY_BTN)

    def tap_connect_now(self):
        self.click(self.CONNECT_NOW_BTN)

    def is_low_battery_icon_displayed(self):
        return self.is_displayed(self.LOW_BATTERY_ICON)

    def enter_supervisor_pin(self, pin):
        self.send_keys(self.SUPERVISOR_PIN_INPUT, pin)
        self.click(self.CONFIRM_PIN_BTN)