import pytest
from src.main.python.pages.login_page import LoginPage
from src.main.python.pages.dashboard_page import DashboardPage

BASE_URL = "https://example.com"   # <-- replace with the real application URL

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login_redirects_to_dashboard(self, driver):
        """Valid credentials should land the user on the dashboard."""
        driver.get(f"{BASE_URL}/login")
        login_page = LoginPage(driver)
        login_page.login("qa_user", "P@ssw0rd")

        # Verify we have been redirected to the dashboard
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_loaded(), "Dashboard did not load after login"
        assert "/dashboard" in driver.current_url, "URL does not contain '/dashboard'"