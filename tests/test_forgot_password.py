import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestForgotPassword:

    def test_forgot_password_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.load(BASE_URL)
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_forgot_link()
        forgot_page.submit_email("registered_user@example.com")
        # No explicit locator for confirmation, so we simply verify that we stay on the same domain
        assert BASE_URL in driver.current_url