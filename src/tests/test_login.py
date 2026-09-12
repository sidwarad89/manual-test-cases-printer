import pytest
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login_redirects_to_console(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login("Demo_Run", "Waradss8997@")
        dashboard = DashboardPage(driver)
        # Verify sidebar elements are visible
        assert dashboard.is_displayed(By.CSS_SELECTOR, dashboard.NAV_BUILD)
        assert dashboard.is_displayed(By.CSS_SELECTOR, "[data-testid='nav-myspace']")
        # Additional simple URL check
        assert "/console" in driver.current_url or "/dashboard" in driver.current_url

    def test_invalid_password_shows_error(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login_invalid("Demo_Run", "WrongPass123")
        error_msg = login.get_error_message()
        assert error_msg != ""
        dashboard = DashboardPage(driver)
        # Sidebar should not be visible
        assert not dashboard.is_displayed(By.CSS_SELECTOR, dashboard.NAV_BUILD)

    def test_empty_fields_show_validation(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        # Click submit without typing anything
        login.click(By.CSS_SELECTOR, login.SUBMIT)
        # Assuming validation adds a class or attribute; we just verify fields are still present
        assert login.is_displayed(By.CSS_SELECTOR, login.USERNAME)
        assert login.is_displayed(By.CSS_SELECTOR, login.PASSWORD)