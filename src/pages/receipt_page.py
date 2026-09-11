from selenium.webdriver.common.by import By
from .base_page import BasePage

class ReceiptPage(BasePage):
    TRANSACTION_DETAILS = (By.ID, "transaction-details")
    PRINT_TIME = (By.ID, "print-time")
    # other receipt related locators can be added as needed

    def get_transaction_details(self):
        return self.get_text(self.TRANSACTION_DETAILS)

    def get_print_time_seconds(self):
        txt = self.get_text(self.PRINT_TIME)
        # Expect format like "3.2s"
        try:
            return float(txt.rstrip('s'))
        except ValueError:
            return None