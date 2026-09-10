from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DashboardPage:
    """Page Object Model for the dashboard page."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.welcome_banner = (By.ID, "welcome-banner")
        self.logout_button = (By.ID, "logout")

    def is_loaded(self) -> bool:
        """Return True if the dashboard is loaded (welcome banner visible)."""
        elements = self.driver.find_elements(*self.welcome_banner)
        return len(elements) > 0

    def get_welcome_text(self) -> str:
        """Return the welcome banner text."""
        return self.driver.find_element(*self.welcome_banner).text

    def logout(self):
        """Click the logout button."""
        self.driver.find_element(*self.logout_button).click()