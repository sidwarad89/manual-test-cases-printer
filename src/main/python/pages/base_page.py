import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def find(self, locator):
        """Find a single element."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Click an element."""
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def send_keys(self, locator, text):
        """Send keys to an element."""
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        """Get text of an element."""
        elem = self.find(locator)
        return elem.text

    def is_displayed(self, locator):
        """Check if element is displayed."""
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    def swipe_up(self, duration=800):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.2
        self.driver.swipe(0, start_y, 0, end_y, duration)

    def pause(self, seconds):
        time.sleep(seconds)