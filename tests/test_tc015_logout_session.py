import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.browser("chrome")
def test_tc015_logout_session(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message()
    # Perform logout
    driver.find_element(By.ID, "logoutBtn").click()
    # Verify redirected to login
    assert driver.current_url.endswith("/login")
    # Try accessing dashboard directly
    driver.get("https://app.example.com/dashboard")
    assert driver.current_url.endswith("/login")