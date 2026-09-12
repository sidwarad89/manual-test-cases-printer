import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.profile_page import ProfilePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestFeedback:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.dismiss_welcome()
        login.login("Demo_Run", "Waradss8997@")
        DashboardPage(driver).click(By.CSS_SELECTOR, "[data-testid='nav-profile']")
        self.profile = ProfilePage(driver)

    def test_submit_feedback_appears_in_list(self, driver):
        message = "Automation test feedback"
        self.profile.submit_feedback(message)
        latest = self.profile.latest_feedback()
        assert message in latest