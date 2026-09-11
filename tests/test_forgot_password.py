import pytest
from config import BASE_URL
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_forgot_password_flow(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.click(LoginPage.FORGOT_LINK)
        forgot = ForgotPasswordPage(driver)
        # Assuming a known test email exists in the system
        forgot.submit_email("demo_user@example.com")
        assert forgot.confirmation_displayed()