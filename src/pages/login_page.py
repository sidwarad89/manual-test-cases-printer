from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    REMEMBER_ME_CHECKBOX = (By.ID, "rememberMe")
    PASSWORD_ERROR = (By.XPATH, "//span[contains(@class,'error') and text()='Password is required']")
    INVALID_CREDENTIALS_TOAST = (By.XPATH, "//div[contains(@class,'toast') and contains(text(),'Invalid credentials')]")
    SQL_INJECTION_ERROR = (By.XPATH, "//div[contains(@class,'error') and contains(text(),'Invalid credentials')]")
    JS_DISABLED_MESSAGE = (By.XPATH, "//div[contains(text(),'JavaScript is required')]")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password")
    PROFILE_ICON = (By.ID, "profileIcon")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def toggle_remember_me(self):
        self.driver.find_element(*self.REMEMBER_ME_CHECKBOX).click()

    def get_password_error(self):
        return self.driver.find_element(*self.PASSWORD_ERROR).text

    def is_invalid_credentials_toast_present(self):
        elems = self.driver.find_elements(*self.INVALID_CREDENTIALS_TOAST)
        return len(elems) > 0

    def is_sql_injection_error_present(self):
        elems = self.driver.find_elements(*self.SQL_INJECTION_ERROR)
        return len(elems) > 0

    def is_js_disabled_message_present(self):
        elems = self.driver.find_elements(*self.JS_DISABLED_MESSAGE)
        return len(elems) > 0

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def is_profile_icon_visible(self):
        elems = self.driver.find_elements(*self.PROFILE_ICON)
        return len(elems) > 0

    def get_login_button_state(self):
        return self.driver.find_element(*self.LOGIN_BUTTON).is_enabled()