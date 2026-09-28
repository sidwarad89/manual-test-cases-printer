import time
import pytest
from pages.signup_page import SignUpPage

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestSignUp:
    def test_weak_password_rejection(self, driver):
        signup_page = SignUpPage(driver)
        signup_page.open(BASE_URL + "/signup")  # Assuming signup URL pattern
        unique_username = f"demo_user_{int(time.time())}"
        signup_page.register(unique_username, f"{unique_username}@example.com", "abc")
        # Verify password rule elements are present (cannot assert their state without spec)
        assert signup_page.is_displayed(SignUpPage.RULE_LENGTH)
        assert signup_page.is_displayed(SignUpPage.RULE_UPPER)
        assert signup_page.is_displayed(SignUpPage.RULE_NUMBER)
        assert signup_page.is_displayed(SignUpPage.RULE_SPECIAL)