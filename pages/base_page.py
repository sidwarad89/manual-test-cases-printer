from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        elem = self.find(locator)
        elem.click()
        return elem

    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)
        return elem

    def get_attribute(self, locator, attribute):
        elem = self.find(locator)
        return elem.get_attribute(attribute)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def is_enabled(self, locator):
        try:
            return self.find(locator).is_enabled()
        except:
            return False