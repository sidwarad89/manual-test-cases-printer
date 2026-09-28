import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.load(BASE_URL)
    return page

def test_forgot_password_flow(login_page):
    forgot_page = ForgotPasswordPage(login_page.driver)
    # Click the forgot password link from login page
    login_page.click(LoginPage.USERNAME)  # ensure focus, then click link
    login_page.click((By.CSS_SELECTOR, '[data-testid="forgot-password-link"]'))
    # Submit a registered email
    email = "demo_run@example.com"
    forgot_page.submit_email(email)

    # Simple verification: email field should be cleared after successful submission
    assert forgot_page.is_email_field_cleared(), "Email field should be cleared after submission"