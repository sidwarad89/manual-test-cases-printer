import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from src.pages.build_page import BuildPage
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_agent_name_updates_progress(driver):
    # Log in first
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

    sidebar = Sidebar(driver)
    build = BuildPage(driver)
    build.open_via_sidebar(sidebar)

    build.set_agent_name("Smoke Agent")
    progress_text = build.get_progress_text()
    assert "Agent Name" in progress_text and "complete" in progress_text.lower()