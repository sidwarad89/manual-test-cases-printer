import pytest
from src.pages.login_page import LoginPage
from src.pages.build_page import BuildPage
from src.pages.sidebar import Sidebar

def test_tc_qap_007_agent_name_progress(driver):
    # Login first
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    # Navigate to Build
    sidebar = Sidebar(driver)
    sidebar.go_to_myspace()  # assuming MySpace leads to dashboard with Build nav
    build = BuildPage(driver)
    build.navigate()
    build.set_agent_name("Smoke Agent")
    # Verify progress indicator updates (simple check that progress text contains '1/')
    progress = build.get_setup_progress_text()
    assert "1/" in progress or "complete" in progress.lower()