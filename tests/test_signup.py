import pytest
from pages.signup_page import SignUpPage

@pytest.mark.usefixtures("driver", "config")
class TestSignUp:
    @pytest.fixture(autouse=True)
    def setup(self, driver, config):
        self.signup_page = SignUpPage(driver)
        self.base_url = config["base_url"]

    def test_weak_password_shows_unmet_rules(self):
        self.signup_page.open(f"{self.base_url}/signup")
        self.signup_page.sign_up("new_user_123", "new_user@example.com", "abc")
        unmet = self.signup_page.get_unmet_rules()
        assert "length" in unmet
        assert "uppercase" in unmet
        assert "number" in unmet
        assert "special" in unmet