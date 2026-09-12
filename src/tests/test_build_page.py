import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.build_page import BuildPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestBuildPage:
    def login_and_navigate_to_build(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login("Demo_Run", "Waradss8997@")
        dashboard = DashboardPage(driver)
        dashboard.go_to_build()
        return BuildPage(driver)

    def test_agent_name_updates_progress(self, driver):
        build = self.login_and_navigate_to_build(driver)
        build.set_agent_name("Smoke Agent")
        progress = build.get_progress_text()
        assert "Agent Name" in progress and "complete" in progress.lower()

    def test_framework_selection_shows_panels(self, driver):
        build = self.login_and_navigate_to_build(driver)
        build.select_framework("Selenium")
        assert build.get_framework_panel_visible("Selenium")

    def test_build_blocked_until_setup_complete(self, driver):
        build = self.login_and_navigate_to_build(driver)
        # Leave agent name blank
        build.click_build_agent()
        assert not build.is_build_agent_enabled()