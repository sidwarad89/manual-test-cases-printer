import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
def test_tc001_login_success(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    dashboard = DashboardPage(driver)
    welcome = dashboard.get_welcome_message()
    assert "testuser" in welcome