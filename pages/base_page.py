from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_attribute(self, locator, attribute):
        elem = self.find(locator)
        return elem.get_attribute(attribute)