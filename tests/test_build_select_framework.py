import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from src.pages.build_page import BuildPage
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_select_framework_shows_samples(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

    sidebar = Sidebar(driver)
    build = BuildPage(driver)
    build.open_via_sidebar(sidebar)

    build.select_framework("Selenium")
    # Verify that sample code panel appears – assume a panel with data-testid='framework-sample'
    sample_panel = (By.CSS_SELECTOR, "[data-testid=framework-sample]")
    elem = build.wait_for_element(sample_panel)
    assert elem.is_displayed()