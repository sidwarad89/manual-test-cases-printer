import pytest
from src.pages.login_page import LoginPage
from src.pages.build_page import BuildPage
from src.pages.sidebar_page import SidebarPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestBuildPage:
    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        driver.get(BASE_URL)
        login = LoginPage(driver)
        login.login("Demo_Run", "Waradss8997@")
        sidebar = SidebarPage(driver)
        sidebar.click_myspace()  # ensure sidebar is loaded
        # navigate to Build
        build = BuildPage(driver)
        build.go_to_build()

    def test_tc_qap_007_agent_name_progress(self, driver):
        build = BuildPage(driver)
        build.set_agent_name("Smoke Agent")
        progress = build.get_progress_text()
        assert "complete" in progress.lower(), "Progress should reflect completed Agent Name"

    def test_tc_qap_008_framework_selection(self, driver):
        build = BuildPage(driver)
        build.select_framework("Selenium")
        # Verify that sample code panel appears – using a generic locator (hypothetical)
        sample_panel = (By.CSS_SELECTOR, '[data-testid="framework-sample"]')
        assert build.is_displayed(sample_panel), "Sample panel for Selenium should be visible"

    def test_tc_qap_009_build_blocked_when_incomplete(self, driver):
        build = BuildPage(driver)
        build.set_agent_name("")  # ensure blank
        enabled = build.is_build_agent_enabled()
        assert not enabled, "Build Agent button should be disabled when required fields are empty"