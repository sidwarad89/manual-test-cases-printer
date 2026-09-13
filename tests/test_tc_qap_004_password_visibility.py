import pytest
from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_tc_qap_004_password_visibility(driver):
    login = LoginPage(driver)
    login.open()
    password_locator = LoginPage.PASSWORD_INPUT
    toggle_locator = (By.CSS_SELECTOR, "[data-testid='login-password-toggle']")
    login.type(password_locator, "Secret123!")
    # Before toggle, type attribute should be password
    assert login.get_attribute(password_locator, "type") == "password"
    login.click(toggle_locator)
    assert login.get_attribute(password_locator, "type") == "text"
    # Toggle back
    login.click(toggle_locator)
    assert login.get_attribute(password_locator, "type") == "password"