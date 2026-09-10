"""Test suite for login functionality."""
import pytest
from src.main.python.pages.login_page import LoginPage
from src.main.python.pages.dashboard_page import DashboardPage


@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.base_url = "https://example.com"   # <-- replace with real URL
        self.driver.get(f"{self.base_url}/login")
        self.login_page = LoginPage(self.driver)

    def test_valid_login_redirects_to_dashboard(self):
        """Valid credentials should land on the dashboard."""
        self.login_page.login("valid_user", "ValidPass123")
        dashboard = DashboardPage(self.driver)
        assert dashboard.is_loaded(), "Dashboard did not load after valid login"
        assert "/dashboard" in dashboard.get_current_url()

    def test_invalid_login_shows_error(self):
        """Invalid credentials must display an error message."""
        self.login_page.login("invalid_user", "wrongPass")
        error = self.login_page.get_error_message()
        assert "Invalid username or password" in error

    @pytest.mark.parametrize(
        "username,password",
        [
            ("", "somePass"),          # empty username
            ("someUser", ""),          # empty password
            ("", ""),                  # both empty
        ],
    )
    def test_login_with_missing_fields(self, username, password):
        """Login should not succeed if any required field is empty."""
        self.login_page.login(username, password)
        # Expect that we are still on login page and an error is shown
        assert "/login" in self.driver.current_url
        error = self.login_page.get_error_message()
        assert "required" in error.lower()