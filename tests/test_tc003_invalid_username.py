import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("edge")
def test_tc003_invalid_username(driver):
    login = LoginPage(driver)
    login.enter_username("nonexistent@example.com")
    login.enter_password("anypass")
    login.click_login()
    assert login.is_invalid_credentials_toast_present()