from selenium.webdriver.common.by import By
from .base_page import BasePage

class PrinterListPage(BasePage):
    PRINTER_ITEMS = (By.ID, "com.example.printerapp:id/printer_item")
    DISCOVERY_PROGRESS = (By.ID, "com.example.printerapp:id/progress_discovery")
    CONNECTED_PRINTER_LABEL = (By.ID, "com.example.printerapp:id/tv_connected_printer")
    ERROR_MESSAGE = (By.ID, "com.example.printerapp:id/tv_error_message")

    def wait_for_discovery(self):
        # Wait until discovery spinner disappears
        self.wait.until(EC.invisibility_of_element_located(self.DISCOVERY_PROGRESS))

    def get_printer_names(self):
        elements = self.driver.find_elements(*self.PRINTER_ITEMS)
        return [el.text for el in elements]

    def select_printer_by_name(self, name):
        elements = self.driver.find_elements(*self.PRINTER_ITEMS)
        for el in elements:
            if el.text == name:
                el.click()
                return True
        return False

    def get_connected_printer_name(self):
        return self.get_text(*self.CONNECTED_PRINTER_LABEL)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)