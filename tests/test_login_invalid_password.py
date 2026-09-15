import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from config import BASE_URL, USER1_USERNAME

def test_sign_in_fails_with_wrong_password(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.login(USER1_USERNAME, "WrongPassword123!")

    error = login.get_error()
    assert error is not None and "invalid" in error.lower()

    # Sidebar should not be visible
    sidebar = Sidebar(driver)
    with pytest.raises(Exception):
        sidebar.wait_for_element(Sidebar.NAV_BUILD)