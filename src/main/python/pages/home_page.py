from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    # Example locators – adjust to actual app UI
    SALES_COMPLETE_BTN = (By.ID, "com.example.posapp:id/btn_complete_sale")
    ORDER_HISTORY_BTN = (By.ID, "com.example.posapp:id/btn_order_history")
    REPRINT_RECEIPT_BTN = (By.ID, "com.example.posapp:id/btn_reprint")
    SELECT_ORDER_ITEM = (By.XPATH, "//android.widget.TextView[@text='{order_id}']")

    def complete_sale(self):
        self.click(self.SALES_COMPLETE_BTN)

    def open_order_history(self):
        self.click(self.ORDER_HISTORY_BTN)

    def select_order(self, order_id):
        locator = (self.SELECT_ORDER_ITEM[0],
                   self.SELECT_ORDER_ITEM[1].format(order_id=order_id))
        self.click(locator)

    def tap_reprint(self):
        self.click(self.REPRINT_RECEIPT_BTN)