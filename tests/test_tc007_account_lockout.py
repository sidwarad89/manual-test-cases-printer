import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc007_account_lockout(driver):
    login = LoginPage(driver)
    for attempt in range(5):
        login.enter_username("testuser")
        login.enter_password("WrongPass1")
        login.click_login()
        # Assuming generic error appears
        assert login.is_invalid_credentials_toast_present()
    # 6th attempt
    login.enter_username("testuser")
    login.enter_password("WrongPass1")
    login.click_login()
    lock_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Account locked')]").text
    assert "Account locked due to multiple failed login attempts" in lock_msg