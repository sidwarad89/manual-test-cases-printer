import pytest
from config import BASE_URL, USERS
from pages.login_page import LoginPage
from pages.sidebar import Sidebar

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login(USERS["user1"]["username"], USERS["user1"]["password"])
        # Verify navigation to console by checking sidebar visibility
        sidebar = Sidebar(driver)
        assert sidebar.is_displayed(Sidebar.NAV_BUILD)

    def test_invalid_password(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(USERS["user1"]["username"], "wrongPassword123")
        assert login.login_error_present()
        sidebar = Sidebar(driver)
        assert not sidebar.is_displayed(Sidebar.NAV_BUILD)

    def test_empty_fields(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.click(LoginPage.SUBMIT_BUTTON)
        # Assuming validation adds error indicators; we just ensure we stay on login page
        assert login.is_displayed(LoginPage.USERNAME_INPUT)
        assert login.is_displayed(LoginPage.PASSWORD_INPUT)

    def test_password_visibility_toggle(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        sample_pass = "Secret123!"
        login.type(LoginPage.PASSWORD_INPUT, sample_pass)
        # Initially should be password type
        assert login.password_field_type() == "password"
        login.toggle_password_visibility()
        assert login.password_field_type() == "text"
        # Toggle back
        login.toggle_password_visibility()
        assert login.password_field_type() == "password"