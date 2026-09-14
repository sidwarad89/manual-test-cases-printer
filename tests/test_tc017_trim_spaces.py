import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
def test_tc017_trim_spaces(driver):
    login = LoginPage(driver)
    login.enter_username("  testuser  ")
    login.enter_password("  Password123!  ")
    login.click_login()
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message()