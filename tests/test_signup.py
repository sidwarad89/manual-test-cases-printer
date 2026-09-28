import time
import pytest
from pages.signup_page import SignUpPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.fixture
def signup_page(driver):
    page = SignUpPage(driver)
    # Assuming sign‑up URL is /signup
    page.load(f"{BASE_URL}/signup")
    return page

def test_signup_weak_password(signup_page):
    timestamp = int(time.time())
    username = f"demo_user_{timestamp}"
    email = f"{username}@example.com"
    weak_password = "abc"
    signup_page.sign_up(username, email, weak_password)

    # Verify that password rule elements are visible (indicating failure)
    assert signup_page.are_password_rules_visible(), "Password rule indicators should be visible for weak password"