import pytest
from src.pages.login_page import LoginPage
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_password_visibility_toggle(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.type(LoginPage.PASSWORD_INPUT, "Secret123")
    # Initially password field type should be 'password'
    assert login.get_password_field_type() == "password"

    login.toggle_password_visibility()
    assert login.get_password_field_type() == "text"

    login.toggle_password_visibility()
    assert login.get_password_field_type() == "password"