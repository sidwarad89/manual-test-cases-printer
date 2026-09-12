import pytest
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_forgot_password_flow(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.click_forgot_password()
        forgot = ForgotPasswordPage(driver)
        forgot.submit_email("demo_run@example.com")
        confirm = forgot.get_confirmation()
        assert "check your inbox" in confirm.lower()