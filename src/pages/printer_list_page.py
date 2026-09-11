from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PrinterListPage(BasePage):
    # Locator for the list container – adjust to actual UI hierarchy
    PRINTER_LIST_CONTAINER = (By.ID, "com.example.pos:id/printer_list")
    PRINTER_ITEM = (By.XPATH, "//android.widget.TextView[@resource-id='com.example.pos:id/printer_name' and @text='{name}']")

    def wait_for_printer_list(self):
        self.wait.until(EC.visibility_of_element_located(self.PRINTER_LIST_CONTAINER))

    def get_printer_names(self):
        self.wait_for_printer_list()
        items = self.driver.find_elements(By.ID, "com.example.pos:id/printer_name")
        return [item.text for item in items]

    def select_printer_by_name(self, name: str):
        locator = (By.XPATH, self.PRINTER_ITEM[1].format(name=name))
        self.click(locator)