import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.profile_page import ProfilePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def profile_page(driver):
    login = LoginPage(driver)
    login.load(BASE_URL)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    assert console.is_displayed(console.NAV_BUILD)
    # Assume profile navigation is via a sidebar item not listed; directly load profile URL
    driver.get(f"{BASE_URL}/profile")
    return ProfilePage(driver)

def test_submit_feedback(profile_page):
    message = "Automation feedback message"
    profile_page.submit_feedback(message)
    # Verify that after submission the feedback textbox is cleared
    assert profile_page.is_feedback_field_cleared(), "Feedback text area should be cleared after submit"