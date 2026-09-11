from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple):
        element = self.find(locator)
        element.click()

    def send_keys(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text