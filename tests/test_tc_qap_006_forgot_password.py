import pytest
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage

def test_tc_qap_006_forgot_password(driver):
    login = LoginPage(driver)
    login.open()
    forgot = ForgotPasswordPage(driver)
    forgot.click_forgot()
    forgot.submit_email("demo_user@example.com")
    # Assume a confirmation toast appears with data-testid='forgot-confirm'
    confirm = (By.CSS_SELECTOR, "[data-testid='forgot-confirm']")
    assert forgot.is_displayed(confirm)