import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_forgot_password_flow(self, driver):
        login = LoginPage(driver)
        login.open()
        forgot = ForgotPasswordPage(driver)
        forgot.open_forgot()
        # Using the valid user's email (assume same as username for demo)
        forgot.reset("demo_user@example.com")
        # Verify confirmation appears (if defined)
        assert forgot.confirmation_visible(), "Confirmation should be visible after submitting forgot password"