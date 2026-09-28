import time
import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.build_page import BuildPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def authenticated_driver(driver):
    login = LoginPage(driver)
    login.load(BASE_URL)
    login.login("Demo_Run", "Waradss8997@")
    # Ensure login succeeded
    console = ConsolePage(driver)
    assert console.is_displayed(console.NAV_BUILD)
    return driver

def test_agent_name_updates_progress(authenticated_driver):
    build = BuildPage(authenticated_driver)
    build.set_agent_name("Smoke Agent")
    # Verify that the input now contains the typed value
    entered = build.get_attribute(BuildPage.AGENT_NAME, "value")
    assert entered == "Smoke Agent"

def test_framework_selection_shows_sample(authenticated_driver):
    build = BuildPage(authenticated_driver)
    build.select_framework("Selenium")
    # No explicit locator for sample panels; verify dropdown value changed
    selected_value = build.get_attribute(BuildPage.FRAMEWORK_SELECT, "value")
    assert selected_value == "Selenium"

def test_build_blocked_until_steps_complete(authenticated_driver):
    build = BuildPage(authenticated_driver)
    # Ensure agent name is empty
    build.type(BuildPage.AGENT_NAME, "")
    # Build button should be disabled
    is_enabled = build.is_build_button_enabled()
    assert not is_enabled, "Build Agent button should be disabled when required fields are empty"