import os
import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.load(BASE_URL)
    return page

def test_login_positive(login_page):
    username = "Demo_Run"
    password = "Waradss8997@"
    login_page.login(username, password)

    # After successful login, sidebar should be visible
    console = ConsolePage(login_page.driver)
    assert console.is_displayed(console.NAV_BUILD), "Build navigation should be visible after login"

def test_login_wrong_password(login_page):
    username = "Demo_Run"
    password = "WrongPassword!"
    login_page.login_with_invalid_password(username, password)

    assert login_page.is_error_displayed(), "Error message should be displayed for wrong password"

def test_login_empty_fields(login_page):
    # Ensure fields are empty
    login_page.type(LoginPage.USERNAME, "")
    login_page.type(LoginPage.PASSWORD, "")
    login_page.click(LoginPage.SUBMIT)

    # URL should remain the login page (no navigation)
    assert BASE_URL in login_page.driver.current_url, "Should stay on login page when fields are empty"

def test_password_visibility_toggle(login_page):
    sample_pwd = "SomePassword123!"
    login_page.type(LoginPage.PASSWORD, sample_pwd)
    # Initially password field type should be 'password'
    assert login_page.get_password_field_type() == "password"
    # Toggle visibility
    login_page.toggle_password_visibility()
    assert login_page.get_password_field_type() == "text", "Password field should change to text after toggle"
    # Toggle back
    login_page.toggle_password_visibility()
    assert login_page.get_password_field_type() == "password", "Password field should revert to password type"