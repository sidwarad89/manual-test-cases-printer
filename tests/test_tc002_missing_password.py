import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("firefox")
def test_tc002_missing_password(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("")
    login.click_login()
    assert login.get_password_error() == "Password is required"