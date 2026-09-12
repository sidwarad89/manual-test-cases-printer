from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def type(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)
        return element

    def get_text(self, by, locator):
        element = self.find(by, locator)
        return element.text

    def is_displayed(self, by, locator):
        try:
            return self.find(by, locator).is_displayed()
        except:
            return False