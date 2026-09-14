import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc013_forgot_password_link(driver):
    login = LoginPage(driver)
    login.click_forgot_password()
    assert driver.current_url.endswith("/reset-password")