import pytest
from src.pages.login_page import LoginPage

def test_tc_qap_002_login_wrong_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "WrongPassword123")
    error_text = login.get_error_text()
    assert error_text != ""
    # Sidebar should not be visible
    from src.pages.sidebar import Sidebar
    sidebar = Sidebar(driver)
    assert not sidebar.is_displayed(Sidebar.MYSPACE)