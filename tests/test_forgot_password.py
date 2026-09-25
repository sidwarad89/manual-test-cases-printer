import pytest
from pages.forgot_password_page import ForgotPasswordPage

REGISTERED_EMAIL = "demo_run@example.com"

def test_forgot_password_flow(driver, base_url):
    forgot = ForgotPasswordPage(driver)
    forgot.open(base_url)
    forgot.click_forgot_link()
    forgot.submit_email(REGISTERED_EMAIL)
    confirmation = forgot.get_confirmation()
    assert "check your inbox" in confirmation.lower()