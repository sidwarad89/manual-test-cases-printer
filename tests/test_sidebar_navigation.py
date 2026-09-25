import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:

    @pytest.fixture(autouse=True)
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        return ConsolePage(driver)

    def test_navigation_items(self, driver):
        console = ConsolePage(driver)

        console.go_to_myspace()
        assert console.is_displayed(ConsolePage.NAV_MYSPACE)

        console.go_to_agents()
        assert console.is_displayed(ConsolePage.NAV_AGENTS)

        console.go_to_mcp()
        assert console.is_displayed(ConsolePage.NAV_MCP)

        console.go_to_analytics()
        assert console.is_displayed(ConsolePage.NAV_ANALYTICS)

        console.go_to_support()
        assert console.is_displayed(ConsolePage.NAV_SUPPORT)