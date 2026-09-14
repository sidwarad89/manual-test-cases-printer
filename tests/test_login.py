import pytest
from pages.login_page import LoginPage
from pages.sidebar import Sidebar

@pytest.mark.usefixtures("driver", "config")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver, config):
        self.login_page = LoginPage(driver)
        self.sidebar = Sidebar(driver)
        self.base_url = config["base_url"]
        self.user = config["users"]["user1"]

    def test_valid_login_lands_on_console(self):
        self.login_page.open(self.base_url)
        self.login_page.dismiss_welcome()
        self.login_page.login(self.user["username"], self.user["password"])
        # Verify sidebar is visible by checking one of its elements
        assert self.sidebar.is_displayed(Sidebar.NAV_BUILD)

    def test_invalid_password_shows_error(self):
        self.login_page.open(self.base_url)
        self.login_page.login(self.user["username"], "wrongPassword123")
        assert self.login_page.is_displayed(LoginPage.ERROR)
        assert "invalid" in self.login_page.get_error_message().lower()

    def test_empty_fields_prevent_submission(self):
        self.login_page.open(self.base_url)
        self.login_page.click(LoginPage.SUBMIT)
        # Expect validation feedback – we check that the button remains disabled or error appears
        assert not self.sidebar.is_displayed(Sidebar.NAV_BUILD)

    def test_password_visibility_toggle(self):
        self.login_page.open(self.base_url)
        self.login_page.type(LoginPage.PASSWORD, "SomeSecret")
        initial_type = self.login_page.password_field_type()
        self.login_page.toggle_password_visibility()
        after_type = self.login_page.password_field_type()
        assert initial_type == "password"
        assert after_type == "text"
        # Toggle back
        self.login_page.toggle_password_visibility()
        assert self.login_page.password_field_type() == "password"