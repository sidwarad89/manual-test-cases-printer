from selenium.webdriver.common.by import By
from .base_page import BasePage

class PrinterPage(BasePage):
    # Locators (these are illustrative; real app may differ)
    CONNECT_PRINTER_BTN = (By.ID, "connect-printer-btn")
    DISCOVERY_LIST = (By.ID, "printer-discovery-list")
    PRINTER_ITEM = lambda name: (By.XPATH, f"//li[contains(@class,'printer-item') and text()='{name}']")
    CONNECT_BTN = (By.ID, "printer-connect-btn")
    STATUS_INDICATOR = (By.ID, "printer-status")
    RETRY_BTN = (By.ID, "retry-connection-btn")
    LOW_BATTERY_ICON = (By.ID, "low-battery-icon")
    FIRMWARE_WARNING = (By.ID, "firmware-warning")
    DISCONNECT_MSG = (By.ID, "disconnect-message")
    DUPLICATE_WATERMARK = (By.ID, "duplicate-watermark")
    SUPERVISOR_PIN_INPUT = (By.ID, "supervisor-pin")
    SUPERVISOR_SUBMIT = (By.ID, "supervisor-submit")
    CONNECTION_CONFLICT_MSG = (By.ID, "connection-conflict")
    RELEASE_CONNECTION_BTN = (By.ID, "release-connection-btn")
    NO_PRINTER_MSG = (By.ID, "no-printer-msg")
    CONNECT_NOW_BTN = (By.ID, "connect-now-btn")
    PRINT_RECEIPT_BTN = (By.ID, "print-receipt-btn")
    PRINT_STATUS = (By.ID, "print-status")
    PAPER_OUT_ERROR = (By.ID, "paper-out-error")
    RETRY_PRINT_BTN = (By.ID, "retry-print-btn")
    BLUETOOTH_TOGGLE = (By.ID, "bluetooth-toggle")
    LOGS_BUTTON = (By.ID, "view-logs-btn")
    LOG_CONTENT = (By.ID, "log-content")

    def open_printer_section(self):
        self.click(self.CONNECT_PRINTER_BTN)

    def wait_for_discovery(self):
        self.find(self.DISCOVERY_LIST)

    def select_printer(self, printer_name):
        self.click(self.PRINTER_ITEM(printer_name))

    def confirm_connection(self):
        self.click(self.CONNECT_BTN)

    def get_status_text(self):
        return self.get_text(self.STATUS_INDICATOR)

    def get_no_printer_message(self):
        return self.get_text(self.NO_PRINTER_MSG)

    def click_connect_now(self):
        self.click(self.CONNECT_NOW_BTN)

    def trigger_print(self):
        self.click(self.PRINT_RECEIPT_BTN)

    def get_print_status(self):
        return self.get_text(self.PRINT_STATUS)

    def get_error_message(self):
        return self.get_text(self.PAPER_OUT_ERROR)

    def retry_print(self):
        self.click(self.RETRY_PRINT_BTN)

    def toggle_bluetooth(self, enable: bool):
        # assume toggle is a checkbox; clicking toggles
        current_state = self.driver.find_element(*self.BLUETOOTH_TOGGLE).is_selected()
        if current_state != enable:
            self.click(self.BLUETOOTH_TOGGLE)

    def view_logs(self):
        self.click(self.LOGS_BUTTON)

    def get_logs(self):
        return self.get_text(self.LOG_CONTENT)

    def enter_supervisor_pin(self, pin):
        self.type(self.SUPERVISOR_PIN_INPUT, pin)

    def submit_supervisor(self):
        self.click(self.SUPERVISOR_SUBMIT)

    def get_conflict_message(self):
        return self.get_text(self.CONNECTION_CONFLICT_MSG)

    def release_connection(self):
        self.click(self.RELEASE_CONNECTION_BTN)

    def get_low_battery_icon_present(self):
        elements = self.driver.find_elements(*self.LOW_BATTERY_ICON)
        return len(elements) > 0

    def get_firmware_warning(self):
        return self.get_text(self.FIRMWARE_WARNING)

    def get_disconnect_message(self):
        return self.get_text(self.DISCONNECT_MSG)

    def get_duplicate_watermark(self):
        return self.get_text(self.DUPLICATE_WATERMARK)