import pytest
from src.pages.login_page import LoginPage
from src.pages.profile_page import ProfilePage

def test_tc_qap_012_logout_security(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    profile = ProfilePage(driver)
    profile.open()
    profile.logout()
    # After logout, should be back at login page
    assert "login" in driver.current_url
    # Attempt to go back
    driver.back()
   