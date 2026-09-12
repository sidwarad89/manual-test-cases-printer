from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "[data-testid='login-username']"
    PASSWORD = "[data-testid='login-password']"
    SUBMIT = "[data-testid='login-submit']"
    ERROR = "[data-testid='login-error']"
    FORGOT_LINK = "[data-testid='forgot-password-link']"

    def open(self, url):
        self.driver.get(url)

    def dismiss_welcome(self):
        # Assuming a generic welcome splash that can be dismissed with ESC or a known button.
        # If not present, this will timeout quietly.
        try:
            self.driver.switch_to.alert.dismiss()
        except:
            pass

    def login(self, username, password):
        self.type(By.CSS_SELECTOR, self.USERNAME, username)
        self.type(By.CSS_SELECTOR, self.PASSWORD, password)
        self.click(By.CSS_SELECTOR, self.SUBMIT)

    def login_invalid(self, username, password):
        self.login(username, password)

    def get_error_message(self):
        return self.get_text(By.CSS_SELECTOR, self.ERROR)

    def click_forgot_password(self):
        self.click(By.CSS_SELECTOR, self.FORGOT_LINK)