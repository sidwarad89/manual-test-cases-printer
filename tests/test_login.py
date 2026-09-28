import os
import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        # Verify console sidebar is visible
        console = ConsolePage(driver)
        assert console.is_displayed(console.NAV_BUILD)

    def test_negative_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL)
        login_page.login("Demo_Run", "WrongPassword123")
        assert login_page.is_displayed(LoginPage.ERROR)
        # Sidebar should not appear
        console = ConsolePage(driver)
        assert not console.is_displayed(console.NAV_BUILD)

    def test_empty_fields_validation(self, driver):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL)
        # Click submit without typing
        login_page.click(LoginPage.SUBMIT)
        # No explicit validation locator; just ensure we stay on login page
        assert driver.current_url == BASE_URL + "/"
        # Ensure error message is not displayed (since no error locator for this case)
        assert not login_page.is_displayed(LoginPage.ERROR)

    def test_password_visibility_toggle(self, driver):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL)
        login_page.type(LoginPage.PASSWORD, "Secret123!")
        # Initially should be password type
        assert login_page.get_password_field_type() == "password"
        login_page.toggle_password_visibility()
        assert login_page.get_password_field_type() == "text"
        # Toggle back
        login_page.toggle_password_visibility()
        assert login_page.get_password_field_type() == "password"