import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_sidebar_navigation_loads_sections(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

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