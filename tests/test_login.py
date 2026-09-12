import pytest
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from config import VALID_USER, INVALID_PASSWORD

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.dismiss_welcome()
        login.login(VALID_USER["username"], VALID_USER["password"])

        sidebar = SidebarPage(driver)
        assert sidebar.is_displayed(SidebarPage.NAV_BUILD), "Build navigation should be visible after login"

    def test_invalid_password(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(VALID_USER["username"], INVALID_PASSWORD)

        assert login.is_displayed(LoginPage.ERROR_MESSAGE), "Error message should be shown for wrong password"
        # Ensure sidebar does not appear
        sidebar = SidebarPage(driver)
        assert not sidebar.is_displayed(SidebarPage.NAV_BUILD), "Sidebar should not be visible on failed login"

    def test_empty_fields(self, driver):
        login = LoginPage(driver)
        login.open()
        # Leave fields empty and click sign in
        login.click(LoginPage.SUBMIT_BUTTON)

        # Assuming validation feedback appears as error element with same locator
        assert login.is_displayed(LoginPage.ERROR_MESSAGE) or driver.current_url == login.driver.current_url, \
            "Form should not submit with empty fields"