import pytest
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage
from config import BASE_URL

def test_forgot_password_flow(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.click_forgot_password()

    forgot = ForgotPasswordPage(driver)
    forgot.submit_email("registered@example.com")  # placeholder email
    confirmation = forgot.get_confirmation()
    assert confirmation is not None and "check your inbox" in confirmation.lower()