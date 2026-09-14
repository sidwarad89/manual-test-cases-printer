import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.config import BASE_URL

@pytest.mark.browser("chrome")
def test_tc009_remember_me():
    # First session with remember me
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.toggle_remember_me()
    login.click_login()
    # Verify login succeeded
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message()
    # Close and reopen browser
    driver.quit()
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    # Should be automatically logged in
    dashboard = DashboardPage(driver)
    assert "testuser" in dashboard.get_welcome_message()
    driver.quit()