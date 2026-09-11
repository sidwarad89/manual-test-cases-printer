import pytest
from config import BASE_URL, USERS
from pages.login_page import LoginPage
from pages.sidebar import Sidebar

@pytest.mark.usefixtures("driver")
class TestSidebarNavigation:
    @pytest.fixture(autouse=True)
    def login(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(USERS["user1"]["username"], USERS["user1"]["password"])
        yield

    def test_sidebar_links_load_sections(self, driver):
        sidebar = Sidebar(driver)

        sidebar.go_to_myspace()
        assert "/myspace" in driver.current_url

        sidebar.go_to_agents()
        assert "/agents" in driver.current_url

        sidebar.go_to_mcp()
        assert "/mcp-tools" in driver.current_url

        sidebar.go_to_analytics()
        assert "/analytics" in driver.current_url

        sidebar.go_to_support()
        assert "/support" in driver.current_url