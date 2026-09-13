import pytest
from src.pages.signup_page import SignupPage
import uuid

def test_tc_qap_005_signup_weak_password(driver):
    signup = SignupPage(driver)
    signup.open()
    unique_user = f"user_{uuid.uuid4().hex[:6]}"
    signup.signup(unique_user, f"{unique_user}@example.com", "abc")
    rules = signup.password_rules()
    assert not all(rules.values()), "All password rules should not be satisfied for weak password"