import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar

def test_tc_qap_010_sidebar_navigation(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    sidebar = Sidebar(driver)

    sidebar.go_to_myspace()
    assert "/myspace" in driver.current_url

    sidebar.go_to_agents()
    assert "/agents" in driver.current_url

    sidebar.go_to_mcp()
    assert "/mcp" in driver.current_url

    sidebar.go_to_analytics()
    assert "/analytics" in driver.current_url

    sidebar.go_to_support()
    assert "/support" in driver.current_url