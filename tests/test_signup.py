import pytest
import uuid
from pages.signup_page import SignUpPage

@pytest.mark.usefixtures("driver")
class TestSignUp:
    def test_weak_password_rejected(self, driver):
        signup = SignUpPage(driver)
        signup.open()
        unique_user = f"user_{uuid.uuid4().hex[:6]}"
        signup.sign_up(unique_user, f"{unique_user}@example.com", "abc")
        rules = signup.password_rules()
        assert not all(rules.values()), "All password rule indicators should show unmet rules for weak password"