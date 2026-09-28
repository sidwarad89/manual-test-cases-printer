import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def logged_in_console(driver):
    login = LoginPage(driver)
    login.load(BASE_URL)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    assert console.is_displayed(console.NAV_BUILD)
    return console

def test_sidebar_navigation(logged_in_console):
    sections = [
        (logged_in_console.NAV_MYSPACE, "myspace"),
        (logged_in_console.NAV_AGENTS, "agents"),
        (logged_in_console.NAV_MCP, "mcp-tools"),
        (logged_in_console.NAV_ANALYTICS, "analytics"),
        (logged_in_console.NAV_SUPPORT, "support")
    ]
    for locator, expected_fragment in sections:
        logged_in_console.click(locator)
        assert expected_fragment in logged_in_console.driver.current_url.lower(), \
            f"URL should contain '{expected_fragment}' after navigation"