import uuid
import pytest
from config import BASE_URL, USERS
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.profile_page import ProfilePage

@pytest.mark.usefixtures("driver")
class TestFeedback:
    @pytest.fixture(autouse=True)
    def login_and_open_profile(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(USERS["user1"]["username"], USERS["user1"]["password"])
        sidebar = Sidebar(driver)
        # Assuming profile page is reachable via a navigation item or URL
        driver.get(f"{BASE_URL}/profile")
        yield

    def test_submit_feedback_appears_in_list(self, driver):
        profile = ProfilePage(driver)
        message = f"Test feedback {uuid.uuid4().hex[:8]}"
        profile.submit_feedback(message)
        assert profile.feedback_appears(message)