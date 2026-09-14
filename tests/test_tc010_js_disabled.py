import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
@pytest.mark.disable_js
def test_tc010_js_disabled(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    # Login button should be disabled or message shown
    assert not login.get_login_button_state() or login.is_js_disabled_message_present()