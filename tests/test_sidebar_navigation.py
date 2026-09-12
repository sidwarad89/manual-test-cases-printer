import pytest
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:
    @pytest.fixture
    def logged_in(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("Demo_Run", "Waradss8997@")
        return SidebarPage(driver)

    def test_navigation_loads_sections(self, logged_in, driver):
        sidebar = logged_in
        # My