import pytest
import uuid
from src.pages.signup_page import SignUpPage

BASE_URL = "https://qa-agent-platform.com/signup"

@pytest.mark.usefixtures("driver")
class TestSignUp:
    def test_weak_password_shows_unmet_rules(self, driver):
        signup = SignUpPage(driver)
        signup.open(BASE_URL)
        unique_user = f"user_{uuid.uuid4().hex[:8]}"
        signup.fill_form(unique_user, f"{unique_user}@example.com", "abc")
        signup.submit()
        rules = signup.get_unmet_rules()
        # All rules should be unmet for password 'abc'
        assert all(rules.values())