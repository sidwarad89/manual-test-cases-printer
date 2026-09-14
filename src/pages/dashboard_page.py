from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class DashboardPage:
    WELCOME_MESSAGE = (By.ID, "welcomeMsg")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_welcome_message(self):
        return self.driver.find_element(*self.WELCOME_MESSAGE).text