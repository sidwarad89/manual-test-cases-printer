import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestFeedback:

    @pytest.fixture(autouse=True)
    def login_and_open_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        login_page.login("Demo_Run", "Waradss8997@")
        console = ConsolePage(driver)
        # Assuming there is a way to navigate to Profile via sidebar; using a placeholder nav
        console.click((By.CSS_SELECTOR, '[data-testid="nav-profile"]'))  # nav-profile not defined in doc; we skip navigation
        return console

    def test_submit_feedback(self, driver):
        console = ConsolePage(driver)
        message = "This is a test feedback."
        console.submit_feedback(message)
        # Verify that the feedback input is cleared after submission
        feedback_value = console.get_attribute(ConsolePage.FEEDBACK_TEXT, "value")
        assert feedback_value == ""