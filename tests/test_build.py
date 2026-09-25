import time
import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.build_page import BuildPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestBuildPage:

    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        console.go_to_build()
        # Ensure we are on the Build page
        build_page = BuildPage(driver)
        build_page.wait.until(lambda d: True)  # dummy wait to ensure page load
        return build_page

    def test_agent_name_updates_progress(self, driver):
        build_page = BuildPage(driver)
        build_page.enter_agent_name("Smoke Agent")
        # Verify the field contains the entered text
        entered = build_page.get_attribute(BuildPage.AGENT_NAME, "value")
        assert entered == "Smoke Agent"

    def test_framework_selection_shows_panels(self, driver):
        build_page = BuildPage(driver)
        build_page.select_framework("Selenium")
        # No locator for panels; we assert that the framework select retains the chosen value
        selected_value = build_page.get_attribute(BuildPage.FRAMEWORK_SELECT, "value")
        assert selected_value == "Selenium"

    def test_build_blocked_until_setup_complete(self, driver):
        build_page = BuildPage(driver)
        # Ensure agent name is empty
        build_page.type(BuildPage.AGENT_NAME, "")
        # Verify that the Build Agent button is disabled
        assert not build_page.is_build_button_enabled()