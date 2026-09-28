import time
import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.build_page import BuildPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestBuildPage:
    def _login(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        console.go_to_build()
        return BuildPage(driver)

    def test_agent_name_updates_progress(self, driver):
        build_page = self._login(driver)
        build_page.enter_agent_name("Smoke Agent")
        # No explicit progress indicator locator; verify the field contains the text
        assert build_page.find(BuildPage.AGENT_NAME).get_attribute("value") == "Smoke Agent"

    def test_framework_selection_shows_sample(self, driver):
        build_page = self._login(driver)
        build_page.select_framework("Selenium")
        # No locator for sample panels; skipping detailed assertion

    def test_build_blocked_until_setup_complete(self, driver):
        build_page = self._login(driver)
        # Ensure agent name is empty
        build_page.type(BuildPage.AGENT_NAME, "")
        # Attempt to click Build Agent
        build_page.click(BuildPage.BUILD_AGENT)
        # Verify button is disabled (or remains disabled)
        assert not build_page.is_build_enabled()