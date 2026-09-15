from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        elem = self.wait_for_element(locator)
        elem.click()
        return elem

    def type(self, locator, text):
        elem = self.wait_for_element(locator)
        elem.clear()
        elem.send_keys(text)
        return elem

    def get_text(self, locator):
        elem = self.wait_for_element(locator)
        return elem.text