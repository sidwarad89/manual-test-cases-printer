from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object Model for the login page."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, url: str):
        """Navigate to the login page."""
        self.driver.get(url)

    def login(self, username: str, password: str):
        """Perform login with supplied credentials."""
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()