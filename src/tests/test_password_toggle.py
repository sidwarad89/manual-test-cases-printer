import pytest
from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By

BASE_URL = "https://qa-agent-platform.com"

@pytest.mark.usefixtures("driver")
class TestPasswordToggle:
    def test_password_visibility_toggle(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        pwd_field = login.find(By.CSS_SELECTOR, login.PASSWORD)
        pwd_field.send_keys("Secret123")
        # Click toggle
        login.click(By.CSS_SELECTOR, "[data-testid='login-password-toggle']")
        # Verify type attribute changed to text
        assert pwd_field.get_attribute("type") == "text"
        # Click again to hide
        login.click(By.CSS_SELECTOR, "[data-testid='login-password-toggle']")
        assert pwd_field.get_attribute("type") == "password"