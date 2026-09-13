import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar

def test_tc_qap_001_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.dismiss_welcome_if_present()
    login.login("Demo_Run", "Waradss8997@")
    # Verify sidebar appears
    sidebar = Sidebar(driver)
    assert sidebar.is_displayed(Sidebar.MYSPACE)
    assert sidebar.is_displayed(Sidebar.BUILD)