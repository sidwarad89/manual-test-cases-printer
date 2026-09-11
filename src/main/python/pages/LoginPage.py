from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):
    """
    Page object representing the login screen of the Android app.
    Update the locators according to the actual app UI.
    """

    # Example locators – replace with real resource‑ids or xpath
    USERNAME_FIELD = (By.ID, "com.example.app:id/username")
    PASSWORD_FIELD = (By.ID, "com.example.app:id/password")
    LOGIN_BUTTON   = (By.ID, "com.example.app:id/loginBtn")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username: str, password: str):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)