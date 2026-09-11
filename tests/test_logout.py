import pytest
from config import BASE_URL, USERS
from pages.login_page import LoginPage
from pages.sidebar import Sidebar

@pytest.mark.usefixtures("driver")
class TestLogout:
    @pytest.fixture(autouse=True)
    def login(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(USERS["user1"]["username"], USERS["user1"]["password"])
        yield

    def test_logout_blocks_back_navigation(self, driver):
        sidebar = Sidebar(driver)
        sidebar.logout()
        # After logout, ensure we are on login page
        assert driver.current_url.rstrip('/') == BASE_URL.rstrip('/')
        # Try navigating back
        driver.back()
        # Should still be on login page
        assert driver.current_url.rstrip('/') == BASE_URL.rstrip('/')