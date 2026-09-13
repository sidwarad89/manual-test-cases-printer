import pytest
from src.pages.signup_page import SignupPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSignupWeakPassword:
    def test_tc_qap_005_weak_password(self, driver):
        driver.get(f"{BASE_URL}/signup")
        signup = SignupPage(driver)
        signup.fill_signup("new_user_123", "new_user_123@example.com", "abc")
        signup.submit()
        rules = signup.get_rule_states()
        # Expect all rules to indicate unmet; exact text depends on implementation
        for key, value in rules.items():
            assert "unmet" in value.lower() or "failed" in value.lower(), f"{key} rule should be unmet"