import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc008_sql_injection(driver):
    login = LoginPage(driver)
    payload = "' OR '1'='1"
    login.enter_username(payload)
    login.enter_password("random")
    login.click_login()
    assert login.is_sql_injection_error_present()