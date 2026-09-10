"""Test suite for dashboard functionality."""
import pytest
from src.main.python.pages.login_page import LoginPage
from src.main.python.pages.dashboard_page import DashboardPage


@pytest.mark.usefixtures("driver")
class TestDashboard:

    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        """Log in once and keep the session for dashboard tests."""
        base_url = "https://example.com"  # <-- replace with real URL
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("valid_user", "ValidPass123")
        self.dashboard = DashboardPage(driver)
        assert self.dashboard.is_loaded(), "Dashboard not loaded in fixture"

    def test_dashboard_welcome_message(self):
        """Verify the welcome banner contains the logged‑in user name."""
        banner = self.dashboard.find(self.dashboard.WELCOME_BANNER).text
        assert "Welcome, valid_user" in banner

    def test_logout_returns_to_login(self):
        """Logout should bring the user back to the login page."""
        self.dashboard.logout()
        # After logout we expect the login page URL
        assert "/login" in self.dashboard.driver.current_url