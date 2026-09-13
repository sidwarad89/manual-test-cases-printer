import pytest
from src.pages.login_page import LoginPage
from src.pages.profile_page import ProfilePage
from src.pages.sidebar_page import SidebarPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestFeedbackSubmission:
    @pytest.fixture(autouse=True)
    def login_and_open_profile(self, driver):
        driver.get(BASE_URL)
        login = LoginPage(driver)
        login.login("Demo_Run", "Waradss8997@")
        sidebar = SidebarPage(driver)
        # Assume there is a profile link in the sidebar
        sidebar.open_profile_menu()
        # Profile page loads automatically

    def test_tc_qap_011_submit_feedback(self, driver):
        profile = ProfilePage(driver)
        test_message = "Automated test feedback"
        profile.submit_feedback