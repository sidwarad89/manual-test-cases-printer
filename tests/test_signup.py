import time
import pytest
from pages.signup_page import SignUpPage

BASE_EMAIL_DOMAIN = "example.com"

def generate_unique_username():
    timestamp = int(time.time() * 1000)
    return f"demo_user_{timestamp}"

def test_signup_weak_password(driver, base_url):
    signup = SignUpPage(driver)
    signup.open(base_url)
    username = generate_unique_username()
    email = f"{username}@{BASE_EMAIL_DOMAIN}"
    signup.fill_form(username, email, "abc")
    signup.submit()
    rules = signup.get_rule_states()
    # All rules should be visible indicating they are unmet
    assert not rules["length"], "Length rule should be unmet"
    assert not rules["upper"], "Uppercase rule should be unmet"
    assert not rules["number"], "Number rule should be unmet"
    assert not rules["special"], "Special character rule should be unmet"