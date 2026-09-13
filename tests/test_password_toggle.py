import pytest
from src.pages.login_page import LoginPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestPasswordToggle:
    def test_tc_qap_004_password_visibility(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.type(LoginPage.PASSWORD, "anySecret")
        initial_type = login_page.get_password_input_type()
        assert initial_type == "password", "Initial type should be password"
        login_page.toggle_password_visibility()
        toggled_type = login_page.get_password_input_type()
        assert toggled_type == "text", "Password should become visible after toggle"
        # Toggle back
        login_page.toggle_password_visibility()
        back_type = login_page.get_password_input_type()
        assert back_type == "password", "Password should hide again after second toggle"