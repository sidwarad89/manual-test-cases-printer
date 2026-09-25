from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-testid="login-username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-testid="login-error"]')

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)