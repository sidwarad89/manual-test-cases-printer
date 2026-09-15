import pytest
import uuid
from src.pages.signup_page import SignupPage
from config import BASE_URL

def test_signup_rejects_weak_password(driver):
    signup = SignupPage(driver)
    signup.open(BASE_URL)

    unique_user = f"user_{uuid.uuid4().hex[:8]}"
    signup.sign_up(unique_user, f"{unique_user}@example.com", "abc")

    statuses = signup.get_all_rules_status()
    # Expect that at least one rule is failing (class indicating failure)
    assert any("fail" in status.lower() for status in statuses.values())