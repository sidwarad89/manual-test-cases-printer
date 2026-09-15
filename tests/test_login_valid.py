import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_sign_in_with_valid_credentials(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

    sidebar = Sidebar(driver)
    # Verify that sidebar elements are visible – checking Build link as representative
    assert sidebar.wait_for_element(Sidebar.NAV_BUILD).is_displayed()