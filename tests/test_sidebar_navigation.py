import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar_page import SidebarPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:
    @pytest.fixture(autouse=True)
    def login(self, driver):
        driver.get(BASE_URL)
        login = LoginPage(driver)
        login.login("Demo_Run", "Waradss8997@")
        # sidebar should now be visible

    def test_tc_qap_010_navigation(self, driver):
        sidebar = SidebarPage(driver)

        # My Space
        sidebar.click_myspace()
        assert "myspace" in driver.current_url.lower()

        # Agents
        sidebar.click_agents()
        assert "agents" in driver.current_url.lower()

        # MCP Tools
        sidebar.click_mcp_tools()
        assert "mcp" in driver.current_url.lower()

        # Analytics
        sidebar.click_analytics()
        assert "analytics" in driver.current_url.lower()

        # Support
        sidebar.click_support()
        assert "support" in driver.current_url.lower()