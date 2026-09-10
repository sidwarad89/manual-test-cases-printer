import json
import os
import pytest
from src.main.python.pages.login_page import LoginPage
from src.main.python.pages.dashboard_page import DashboardPage


@pytest.fixture(scope="module")
def test_data():
    """Load test data from JSON file."""
    data_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "resources", "testdata.json")
    with open(data_path, "r") as f:
        return json.load(f)


def test_valid_login_redirects_to_dashboard(driver, test_data):
    """Valid login should redirect to dashboard and display welcome message."""
    login_url = test_data["login_url"]
    username = test_data["valid_user"]["username"]
    password = test_data["valid_user"]["password"]
    expected_welcome = test_data["valid_user"]["welcome_message"]

    login_page = LoginPage(driver)
    login_page.open(login_url)
    login_page.login(username, password)

    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded(), "Dashboard did not load after login"
    assert expected_welcome in dashboard.get_welcome_text(), "Welcome message mismatch"


def test_invalid_login_shows_error(driver, test_data):
    """Invalid login should stay on login page and show an error alert."""
    login_url = test_data["login_url"]
    username = test_data["invalid_user"]["username"]
    password = test_data["invalid_user"]["password"]
    expected_error = test_data["invalid_user"]["error_message"]

    login_page = LoginPage(driver)
    login_page.open(login_url)
    login_page.login(username, password)

    # Assuming an error alert appears with id="login-error"
    error_alert = driver.find_element(By.ID, "login-error")
    assert error_alert.is_displayed(), "Error alert not displayed for invalid login"
    assert expected_error in error_alert.text, "Error message text is incorrect"