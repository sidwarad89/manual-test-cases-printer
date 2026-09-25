import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.profile_page import ProfilePage

def test_submit_feedback(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    console.click(ConsolePage.NAV_SUPPORT)  # Assuming profile is reachable via Support section
    profile = ProfilePage(driver)
    message = "Automation feedback test"
    profile.submit_feedback(message)
    latest = profile.get_latest_feedback()
    assert message in latest, "Submitted feedback should appear in the feedback list"