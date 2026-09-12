import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login("Demo_Run", "Waradss8997@")
        self.dashboard = DashboardPage(driver)

    def test_each_sidebar_section_loads(self, driver):
        sections = [
            ("nav-myspace", "/myspace"),
            ("nav-agents", "/agents"),
            ("nav-mcp", "/mcp-tools"),
            ("nav-analytics", "/analytics"),
            ("nav-support", "/support"),
        ]
        for testid, fragment in sections:
            self.dashboard.click(By.CSS_SELECTOR, f"[data-testid='{testid}']")
            assert fragment in driver.current_url