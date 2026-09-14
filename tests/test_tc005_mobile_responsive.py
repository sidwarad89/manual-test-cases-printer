import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
@pytest.mark.mobile
def test_tc005_mobile_responsive(driver):
    login = LoginPage(driver)
    # Verify fields are visible
    assert login.driver.find_element(*login.USERNAME_INPUT).is_displayed()
    assert login.driver.find_element(*login.PASSWORD_INPUT).is_displayed()
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    dashboard = DashboardPage(driver)
    welcome = dashboard.get_welcome_message()
    assert "testuser" in welcome