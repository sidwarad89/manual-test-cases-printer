import uuid
import pytest
from pages.signup_page import SignupPage

@pytest.mark.usefixtures("driver")
class TestSignup:
    def test_weak_password_rejected(self, driver):
        signup = SignupPage(driver)
        signup.open("https://qa-agent-platform.com/signup")
        unique_user = f"user_{uuid.uuid4().hex[:6]}"
        email = f"{unique_user}@example.com"
        signup.sign_up(unique_user, email, "abc")
        # Verify that all rule indicators are displayed (failed)
        assert signup.password_rule_failed(SignupPage.RULE_LENGTH)
        assert signup.password_rule_failed(SignupPage.RULE_UPPER)
        assert signup.password_rule_failed(SignupPage.RULE_NUMBER)
        assert signup.password_rule_failed(SignupPage.RULE_SPECIAL)