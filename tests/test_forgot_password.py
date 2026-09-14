import pytest
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "config")
class TestForgotPassword:
    @pytest.fixture(autouse=True)
    def setup(self, driver, config):
        self.forgot_page = ForgotPasswordPage(driver)
        self.login_page = LoginPage(driver)
        self.base_url = config["base_url"]
        self.user = config["users"]["user1"]

    def test_forgot_password_accepts_email(self):
        self.forgot_page.open(self.base_url)
        self.forgot_page.click_forgot_link()
        self.forgot_page.reset_password(self.user["username"] + "@example.com")
        # Assuming a confirmation message appears with data-testid='forgot-confirm'
        CONFIRM = (By.CSS_SELECTOR, "[data-testid='forgot-confirm']")
        assert self.forgot_page.is_displayed(CONFIRM)