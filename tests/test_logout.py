import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

def test_logout_blocks_back_navigation(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    console.click(ConsolePage.LOGOUT_BUTTON)
    # After logout, attempt to go back
    driver.back()
    # Should be back on login page
    assert login.is_visible(LoginPage.SUBMIT), "Login submit button should be visible after logout and back navigation"
    assert "login" in login.get_current_url().lower()