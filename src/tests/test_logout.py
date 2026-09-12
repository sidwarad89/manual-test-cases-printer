import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogout:
    def test_logout_and_back_navigation(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login("Demo_Run", "Waradss8997@")
        dashboard = DashboardPage(driver)
        dashboard.logout()
        # After logout, we should be back on login page
        assert login.is_displayed(By.CSS_SELECTOR, login.USERNAME)
        # Simulate browser back
        driver.back()
        # Should still be on login page (session cleared)
        assert login.is_displayed(By.CSS_SELECTOR, login.USERNAME)