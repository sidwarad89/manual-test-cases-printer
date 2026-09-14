import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc020_profile_icon(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    assert login.is_profile_icon_visible()