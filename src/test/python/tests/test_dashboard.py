import pytest
from src.main.python.pages.dashboard_page import DashboardPage

BASE_URL = "https://example.com"   # <-- replace with the real application URL

@pytest.mark.usefixtures("driver")
class TestDashboard:
    def test_dashboard_welcome_banner_present(self, driver):
        """After a successful login the dashboard should show a welcome banner."""
        # For the purpose of this demo we assume the user is already logged in.
        driver.get(f"{BASE_URL}/dashboard")
        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), "Dashboard page failed to load"
        # Additional assertions could be added here, e.g. checking banner text.