import pytest
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc011_password_mask(driver):
    login = LoginPage(driver)
    password_elem = driver.find_element(*login.PASSWORD_INPUT)
    type_attr = password_elem.get_attribute("type")
    assert type_attr == "password"