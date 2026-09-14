import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
@pytest.mark.incognito
def test_tc004_incognito_success(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message()
    # Verify cookie flags
    cookies = driver.get_cookies()
    session_cookie = next((c for c in cookies if c["name"] == "sessionid"), None)
    assert session_cookie is not None
    assert session_cookie.get("secure") is True
    assert session_cookie.get("httpOnly") is True