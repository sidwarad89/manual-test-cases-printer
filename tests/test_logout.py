import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogout:

    def test_logout_and_back_navigation(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        console.logout()
        # After logout, we should be back on the login page
        assert BASE_URL in driver.current_url
        # Attempt to navigate back
        driver.back()
        # Still should be on login page
        assert BASE_URL in driver.current_url