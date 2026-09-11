from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple

class BasePage:
    """Base page containing common Selenium/Appium actions."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator: Tuple[By, str]):
        """Find a single element."""
        return self.driver.find_element(*locator)

    def click(self, locator: Tuple[By, str]):
        """Click on an element identified by the locator."""
        self.find(locator).click()

    def send_keys(self, locator: Tuple[By, str], text: str):
        """Send text to an input field."""
        self.find(locator).clear()
        self.find(locator).send_keys(text)

    def get_text(self, locator: Tuple[By, str]) -> str:
        """Return text of an element."""
        return self.find(locator).text