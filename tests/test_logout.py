import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogout:
    def test_logout_blocks_back_navigation(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        console.logout()
        # After logout, we should be at login page
        assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
        # Simulate browser back
        driver.execute_script("window.history.back();")
        # Ensure we are still on login page
        assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")