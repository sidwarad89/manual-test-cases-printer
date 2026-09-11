from pages.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class PrinterPage(BasePage):
    # Locators (adjust according to the real app)
    CONNECT_PRINTER_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Connect Printer")
    PRINTER_LIST = (MobileBy.ID, "printer_list")  # container
    PRINTER_ITEM = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='printer_name']")  # generic
    CONNECTED_INDICATOR = (MobileBy.ACCESSIBILITY_ID, "Printer Connected")
    CONNECTION_STATUS = (MobileBy.ID, "connection_status")
    PRINT_RECEIPT_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Print Receipt")
    NO_PRINTER_MESSAGE = (MobileBy.XPATH, "//*[contains(@text, 'No printer connected')]")
    CONNECT_NOW_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Connect Now")
    ERROR_MESSAGE = (MobileBy.ID, "error_message")
    DUPLICATE_WATERMARK = (MobileBy.XPATH, "//*[contains(@text, 'DUPLICATE COPY')]")
    LOW_BATTERY_ICON = (MobileBy.ACCESSIBILITY_ID, "Low Battery")
    SUPERVISOR_PIN_FIELD = (MobileBy.ID, "supervisor_pin")
    SUPERVISOR_OK_BUTTON = (MobileBy.ACCESSIBILITY_ID, "OK")
    RETRY_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Retry")
    # ... other locators as needed

    def open_printer_discovery(self):
        """Tap the Connect Printer button to open discovery UI."""
        self.click(self.CONNECT_PRINTER_BUTTON)

    def get_discovered_printers(self):
        """Return list of printer names displayed."""
        self.wait_for_visibility(self.PRINTER_LIST)
        items = self.finds(self.PRINTER_ITEM)
        return [item.text for item in items]

    def select_printer(self, printer_name):
        """Select a printer from the discovery list by its displayed name."""
        self.wait_for_visibility(self.PRINTER_LIST)
        items = self.finds(self.PRINTER_ITEM)
        for item in items:
            if item.text == printer_name:
                item.click()
                return True
        raise Exception(f"Printer named '{printer_name}' not found in list")

    def is_printer_connected(self):
        """Check if the connected indicator is visible."""
        return self.is_displayed(self.CONNECTED_INDICATOR)

    def get_connection_status_text(self):
        return self.get_text(self.CONNECTION_STATUS)

    def trigger_print(self):
        """Tap the Print Receipt button."""
        self.click(self.PRINT_RECEIPT_BUTTON)

    def get_no_printer_message(self):
        return self.get_text(self.NO_PRINTER_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_duplicate_watermark_displayed(self):
        return self.is_displayed(self.DUPLICATE_WATERMARK)

    def is_low_battery_icon_displayed(self):
        return self.is_displayed(self.LOW_BATTERY_ICON)

    def enter_supervisor_pin(self, pin):
        self.send_keys(self.SUPERVISOR_PIN_FIELD, pin)
        self.click(self.SUPERVISOR_OK_BUTTON)

    def retry_connection(self):
        self.click(self.RETRY_BUTTON)

    # Additional helper methods for specific flows
    def complete_sale_and_print(self):
        """Placeholder: simulate completing a sale then printing."""
        # This would involve many steps; for demo we directly trigger print.
        self.trigger_print()