import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from src.pages.build_page import BuildPage
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_build_blocked_until_setup_complete(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

    sidebar = Sidebar(driver)
    build = BuildPage(driver)
    build.open_via_sidebar(sidebar)

    # Do NOT fill agent name
    assert not build.is_build_agent_enabled()