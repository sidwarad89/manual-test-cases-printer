import pytest
from src.pages.login_page import LoginPage
from src.pages.build_page import BuildPage
from src.pages.sidebar import Sidebar

def test_tc_qap_009_build_blocked(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    sidebar = Sidebar(driver)
    sidebar.go_to_myspace()
    build = BuildPage(driver)
    build.navigate()
    # Leave agent name blank and attempt to click Build Agent
    assert not build.is_build_enabled()