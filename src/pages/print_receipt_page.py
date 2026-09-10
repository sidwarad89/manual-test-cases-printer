from selenium.webdriver.common.by import By
from .base_page import BasePage

class PrintReceiptPage(BasePage):
    PRINT_STATUS = (By.ID, "com.example.printerapp:id/tv_print_status")
    RETRY_BTN = (By.ID, "com.example.printerapp:id/btn_retry")
    CONNECT_NOW_BTN = (By.ID, "com.example.printerapp:id/btn_connect_now")
    DUPLICATE_WATERMARK = (By.ID, "com.example.printerapp:id/tv_duplicate_watermark")
    SUPERVISOR_PIN_INPUT = (By.ID, "com.example.printerapp:id/input_supervisor_pin")
    SUBMIT_PIN_BTN = (By.ID, "com.example.printerapp:id/btn_submit_pin")
    ERROR_MESSAGE = (By.ID, "com.example.printerapp:id/tv_error_message")

    def wait_for_print_completion(self, timeout=10):
        self.wait.until(EC.text_to_be_present_in_element(self.PRINT_STATUS, "Printed"))

    def get_print_status(self):
        return self.get_text(*self.PRINT_STATUS)

    def tap_retry(self):
        self.click(*self.RETRY_BTN)

    def tap_connect_now(self):
        self.click(*self.CONNECT_NOW_BTN)

    def is_duplicate_watermark_displayed(self):
        return self.is_displayed(*self.DUPLICATE_WATERMARK)

    def enter_supervisor_pin(self, pin):
        self.send_keys(*self.SUPERVISOR_PIN_INPUT, pin)

    def submit_supervisor_pin(self):
        self.click(*self.SUBMIT_PIN_BTN)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)