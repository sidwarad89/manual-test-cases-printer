import pytest
from pages.console_page import ConsolePage
from pages.build_page import BuildPage

def test_build_agent_name_progress(driver, base_url):
    # Login first
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    console.click(ConsolePage.NAV_BUILD)
    build = BuildPage(driver)
    build.enter_agent_name("Smoke Agent")
    progress_text = build.get_progress_text()
    assert "Smoke Agent" in progress_text

def test_framework_selection_shows_panels(driver, base_url):
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    console.click(ConsolePage.NAV_BUILD)
    build = BuildPage(driver)
    build.select_framework("Selenium")
    assert build.is_sample_visible(), "Sample panel should appear for Selenium"
    assert build.is_prereq_visible(), "Prerequisite panel should appear for Selenium"

def test_build_agent_button_disabled_without_name(driver, base_url):
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    console.click(ConsolePage.NAV_BUILD)
    build = BuildPage(driver)
    # Ensure agent name is empty
    build.type(BuildPage.AGENT_NAME, "")
    assert not build.is_build_agent_enabled(), "Build Agent button should be disabled when required fields are empty"