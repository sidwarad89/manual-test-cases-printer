import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

VALID_USER = {"username": "Demo_Run", "password": "Waradss8997@"}
INVALID_PASSWORD = "wrongPassword123"

def test_login_success(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(VALID_USER["username"], VALID_USER["password"])
    console = ConsolePage(driver)
    assert console.is_sidebar_visible(), "Sidebar should be visible after successful login"
    assert "console" in login.get_current_url(), "URL should contain 'console' after login"

def test_login_invalid_password(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(VALID_USER["username"], INVALID_PASSWORD)
    error = login.get_error_message()
    assert error != "", "An error message should be displayed for invalid credentials"
    assert "invalid" in error.lower() or "incorrect" in error.lower()

def test_login_empty_fields(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    # Do not type anything, just click submit
    login.click(LoginPage.SUBMIT)
    # Expect validation feedback; using same submit button as locator for simplicity
    assert login.is_visible(LoginPage.USERNAME), "Username field should still be visible (validation failed)"
    assert login.is_visible(LoginPage.PASSWORD), "Password field should still be visible (validation failed)"

def test_password_visibility_toggle(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    # Input a known password
    login.type(LoginPage.PASSWORD, "Secret123!")
    # Click toggle
    login.click((By.CSS_SELECTOR, '[data-testid="login-password-toggle"]'))
    # Verify input type changed to text
    password_element = login.find(LoginPage.PASSWORD)
    assert password_element.get_attribute("type") == "text"
    # Toggle back
    login.click((By.CSS_SELECTOR, '[data-testid="login-password-toggle"]'))
    assert password_element.get_attribute("type") == "password"