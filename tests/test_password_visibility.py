import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestPasswordVisibility:
    def test_toggle_password_visibility(self, driver):
        login = LoginPage(driver)
        login.open()
        login.type(LoginPage.PASSWORD_INPUT, "SomePass123")
        # initial type should be password
        assert login.password_input_type() == "password"
        login.toggle_password_visibility()
        assert login.password_input_type() == "text"
        # toggle back
        login.toggle_password_visibility()
        assert login.password_input_type() == "password"