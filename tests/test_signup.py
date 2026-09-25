import time
import pytest
from pages.signup_page import SignUpPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSignUp:

    def test_weak_password_rejection(self, driver):
        signup_page = SignUpPage(driver)
        signup_page.load(f"{BASE_URL}/signup")
        unique_username = f"demo_user_{int(time.time())}"
        signup_page.fill_form(unique_username, "demo@example.com", "abc")
        signup_page.submit()
        # Verify that each password rule element is visible (indicating unmet rule)
        assert signup_page.password_rule_is_visible(SignUpPage.PASSWORD_RULE_LENGTH)
        assert signup_page.password_rule_is_visible(SignUpPage.PASSWORD_RULE_UPPER)
        assert signup_page.password_rule_is_visible(SignUpPage.PASSWORD_RULE_NUMBER)
        assert signup_page.password_rule_is_visible(SignUpPage.PASSWORD_RULE_SPECIAL)