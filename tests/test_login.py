import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar_page import SidebarPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_tc_qap_001_valid_login(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.dismiss_welcome_splash()
        login_page.login("Demo_Run", "Waradss8997@")
        sidebar = SidebarPage(driver)
        assert sidebar.is_displayed(SidebarPage.MY_SPACE), "Sidebar should be visible after login"

    def test_tc_qap_002_invalid_password(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.login("Demo_Run", "wrongPassword123")
        assert login_page.is_displayed(LoginPage.ERROR), "Error message should be displayed"
        sidebar = SidebarPage(driver)
        assert not sidebar.is_displayed(SidebarPage.MY_SPACE), "Sidebar must not appear on failed login"

    def test_tc_qap_003_empty_fields(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.login("", "")
        # Expect the login page to stay; we verify that the URL has not changed to contain '/dashboard' or similar
        assert "login" in driver.current_url.lower(), "Should stay on login page when fields are empty"