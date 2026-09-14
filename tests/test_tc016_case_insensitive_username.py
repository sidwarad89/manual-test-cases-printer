import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
def test_tc016_case_insensitive_username(driver):
    login = LoginPage(driver)
    login.enter_username("TestUser")  # different case
    login.enter_password("Password123!")
    login.click_login()
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message().lower()