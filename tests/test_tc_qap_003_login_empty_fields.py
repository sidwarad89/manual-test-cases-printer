import pytest
from src.pages.login_page import LoginPage

def test_tc_qap_003_login_empty_fields(driver):
    login = LoginPage(driver)
    login.open()
    login.login("", "")
    # Expect validation feedback; we just assert that we stay on login page
    assert "login" in driver.current_url