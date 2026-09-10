from selenium.webdriver.common.by import By
from .base_page import BasePage

class PrinterListPage(BasePage):
    """Page showing discoverable/paired printers."""

    PRINTER_ROWS = (By.CSS_SELECTOR, ".printer-row")
    PRINTER_NAME = (By.CSS_SELECTOR, ".printer-name")
    CONNECT_BTN = (By.CSS_SELECTOR, ".connect-btn")
    NO_PRINTER_MSG = (By.ID, "no_printer_msg")

    def get_printer_names(self):
        """Return list of printer names displayed."""
        rows = self.driver.find_elements(*self.PRINTER_ROWS)
        return [row.find_element(*self.PRINTER_NAME).text for row in rows]

    def select_printer_by_name(self, name):
        """Select printer matching the given name."""
        rows = self.driver.find_elements(*self.PRINTER_ROWS)
        for row in rows:
            if row.find_element(*self.PRINTER_NAME).text == name:
                row.find_element(*self.CONNECT_BTN).click()
                return True
        return False

    def is_no_printer_message_displayed(self):
        return self.is_displayed(self.NO_PRINTER_MSG)