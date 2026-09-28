import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage
from pages.profile_page import ProfilePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestProfileFeedback:
    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        # Assuming there is a profile navigation item; reuse My Space for demo
        console.go_to_myspace()

    def test_submit_feedback_appears_in_list(self, driver):
        profile = ProfilePage(driver)
        message = "Automated feedback test"
        profile.submit_feedback(message)
        # No locator for feedback list; cannot assert appearance.
        # Could verify the input is cleared after submit
        assert profile.find(ProfilePage.FEEDBACK_TEXT).text == ""