import pytest
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_tc_qap_006_forgot_password(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        forgot = ForgotPasswordPage(driver)
        forgot.open_forgot_form()
        forgot.submit_email("demo_user@example.com")
        assert forgot.confirmation_is_displayed(), "Confirmation message should be shown"