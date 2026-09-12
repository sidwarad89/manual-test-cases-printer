import pytest
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from pages.build_page import BuildPage

@pytest.mark.usefixtures("driver")
class TestBuildPage:
    @pytest.fixture
    def logged_in(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("Demo_Run", "Waradss8997@")
        sidebar = SidebarPage(driver)
        sidebar.click_build()
        return BuildPage(driver)

    def test_agent_name_updates_progress(self, logged_in):
        build = logged_in
        build.set_agent_name("Smoke Agent")
        progress_text = build.get_progress_text()
        assert "Agent Name" in progress_text and "complete" in progress_text.lower(), \
            "Progress should reflect completed Agent Name step"

    def test_select_framework_shows_sample(self, logged_in):
        build = logged_in
        build.select_framework("Selenium")
        assert build.sample_panel_visible(), "Sample panel should be visible after selecting Selenium framework"

    def test_build_blocked_until_setup_complete(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("Demo_Run", "Waradss8997@")
        sidebar = SidebarPage(driver)
        sidebar.click_build()
        build = BuildPage(driver)
        # Ensure agent name is empty
        build.type(BuildPage.AGENT_NAME_INPUT, "")
        assert not build.is_build_enabled(), "Build button should be disabled when required fields are empty"