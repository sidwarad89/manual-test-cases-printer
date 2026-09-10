"""Login related test cases."""

import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get("https://example.com/login")  # Adjust URL as needed
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    def test_valid_login_redirects_to_dashboard(self):
        """Valid credentials should take the user to the dashboard."""
        self.login_page.login("qa_user", "P@ssw0rd")
        # Simple wait for navigation
        WebDriverWait(self.driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        assert "/dashboard" in self.driver.current_url
        assert self.dashboard_page.is_loaded()

    def test_invalid_login_shows_error_message(self):
        """Invalid credentials must display an error."""
        self.login_page.login("wrong_user", "badPassword")
        error = self.login_page.get_error_message()
        assert error is not None
        assert "Invalid username or password" in error