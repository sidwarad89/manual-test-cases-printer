from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()
        return element

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_attribute(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    def is_displayed(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False