import pytest
import uuid
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from src.pages.profile_page import ProfilePage
from config import BASE_URL, USER1_USERNAME, USER1_PASSWORD

def test_submit_feedback_appears_in_list(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, USER1_PASSWORD)

    sidebar = Sidebar(driver)
    # Assuming there is a nav item for profile – using placeholder method
    # sidebar.go_to_profile()  # Not defined; replace with direct navigation if needed
    driver.get(f"{BASE_URL}/profile")

    profile = ProfilePage(driver)
    message = f"Feedback {uuid.uuid4().hex[:6]}"
    profile.submit_feedback(message)

    latest = profile.get_latest_feedback()
    assert message in latest
    assert "awaiting a reply" in latest.lower()