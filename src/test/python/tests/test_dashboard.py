import os
import json
import pytest
from src.main.python.pages.login_page import LoginPage
from src.main.python.pages.dashboard_page import DashboardPage


@pytest.fixture(scope="module")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "resources", "testdata.json")
    with open(data_path, "r") as f:
        return json.load(f)


def test_dashboard_logout_returns_to_login(driver, test_data):
    """After successful login, clicking logout should return user to login page."""
    login_url = test_data["login_url"]
    username = test_data["valid_user"]["username"]
    password = test_data["valid_user"]["password"]

    login_page = LoginPage(driver)
    login_page.open(login_url)
    login_page.login(username, password)

    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded(), "Dashboard not loaded after login"

    dashboard.logout()

    # Verify we are back on the login page (e.g., username field is present)
    assert driver.find_element(*login_page.username_input).is_displayed()