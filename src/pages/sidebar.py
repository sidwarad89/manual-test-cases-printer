from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class Sidebar(BasePage):
    # Generic method – receives the data-testid string
    def click_item(self, testid):
        locator = (By.CSS_SELECTOR, f"[data-testid={testid}]")
        self.click(locator)

    def is_item_visible(self, testid):
        locator = (By.CSS_SELECTOR, f"[data-testid={testid}]")
        return self.is_visible(locator)