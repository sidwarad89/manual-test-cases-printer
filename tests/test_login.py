import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        # Verify that the Build navigation item is visible, indicating successful login
        assert console.is_displayed(ConsolePage.NAV_BUILD)

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login_with_invalid_password("Demo_Run", "WrongPassword123")
        # Verify that error message is shown and user stays on login page
        assert login_page.is_displayed(LoginPage.ERROR)

    def test_empty_fields(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.click(LoginPage.SUBMIT)
        # No new locator for validation, so assert that we are still on the login URL
        assert driver.current_url == BASE_URL

    def test_password_visibility_toggle(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.type(LoginPage.PASSWORD, "Secret123!")
        initial_type = login_page.get_password_input_type()
        assert initial_type == "password"
        login_page.toggle_password_visibility()
        toggled_type = login_page.get_password_input_type()
        assert toggled_type == "text"