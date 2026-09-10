"""Dashboard related test cases."""

import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestDashboard:

    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        """Log in once before each test."""
        driver.get("https://example.com/login")
        login_page = LoginPage(driver)
        login_page.login("qa_user", "P@ssw0rd")
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        self.dashboard_page = DashboardPage(driver)

    def test_dashboard_welcome_banner_displayed(self):
        """Verify that the welcome banner is visible after login."""
        assert self.dashboard_page.is_loaded()
        banner = self.dashboard_page.find(self.dashboard_page.WELCOME_BANNER)
        assert banner.is_displayed()
        assert "Welcome" in banner.text

    def test_logout_returns_to_login(self):
        """Logout should navigate back to the login page."""
        self.dashboard_page.logout()
        WebDriverWait(self.dashboard_page.driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in self.dashboard_page.driver.current_url