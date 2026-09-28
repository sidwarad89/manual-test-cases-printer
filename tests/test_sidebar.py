import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:
    @pytest.fixture(autouse=True)
    def login_and_prepare(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login("Demo_Run", "Waradss8997@")

    def test_sidebar_links_load_sections(self, driver):
        console = ConsolePage(driver)

        console.go_to_myspace()
        assert "myspace" in driver.current_url.lower()

        console.go_to_agents()
        assert "agents" in driver.current_url.lower()

        console.go_to_mcp()
        assert "mcp" in driver.current_url.lower()

        console.go_to_analytics()
        assert "analytics" in driver.current_url.lower()

        console.go_to_support()
        assert "support" in driver.current_url.lower()