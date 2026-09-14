import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc006_https_enforced(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    # Ensure we are still on HTTPS
    assert driver.current_url.startswith("https://")
    # No plaintext credentials in URL
    assert "Password123!" not in driver.current_url