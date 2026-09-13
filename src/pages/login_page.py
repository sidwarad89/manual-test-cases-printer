from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid='login-username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='login-password']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid='login-submit']")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-testid='login-error']")
    WELCOME_SPLASH = (By.CSS_SELECTOR, "[data-testid='welcome-splash']")  # assumed

    def open(self):
        from src.config import BASE_URL
        self.driver.get(BASE_URL)

    def dismiss_welcome_if_present(self):
        if self.is_displayed(self.WELCOME_SPLASH):
            self.click(self.WELCOME_SPLASH)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    def get_error_text(self):
        return self.find(self.ERROR_MSG).text