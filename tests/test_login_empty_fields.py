import pytest
from src.pages.login_page import LoginPage
from src.pages.sidebar import Sidebar
from config import BASE_URL

def test_sign_in_blocked_when_fields_empty(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.dismiss_welcome_splash()
    login.click(login.SUBMIT_BUTTON)

    # Expect validation feedback – we assume error element appears
    error = login.get_error()
    assert error is not None and "required" in error.lower()

    sidebar = Sidebar(driver)
    with pytest.raises(Exception):
        sidebar.wait_for_element(Sidebar.NAV_BUILD)