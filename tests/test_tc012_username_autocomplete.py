import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc012_username_autocomplete(driver):
    login = LoginPage(driver)
    username_elem = driver.find_element(*login.USERNAME_INPUT)
    autocomplete = username_elem.get_attribute("autocomplete")
    assert autocomplete == "off"