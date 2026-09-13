import pytest
from src.pages.login_page import LoginPage
from src.pages.build_page import BuildPage
from src.pages.sidebar import Sidebar

def test_tc_qap_008_framework_selection(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    sidebar = Sidebar(driver)
    sidebar.go_to_myspace()
    build = BuildPage(driver)
    build.navigate()
    build.select_framework("Selenium")
    # Verify sample panels appear – assume panel has data-testid='framework-sample'
    sample_panel = (By.CSS_SELECTOR, "[data-testid='framework-sample']")
    assert build.is_displayed(sample_panel)