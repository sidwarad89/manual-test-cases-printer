import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc019_post_logout_redirect(driver):
    login = LoginPage(driver)
    login.enter_username("testuser")
    login.enter_password("Password123!")
    login.click_login()
    driver.find_element(By.ID, "logoutBtn").click()
    # Attempt to go to dashboard
    driver.get("https://app.example.com/dashboard")
    assert driver.current_url.endswith("/login")