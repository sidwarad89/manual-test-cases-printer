import pytest
from config import BASE_URL, USERS
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.build_page import BuildPage

@pytest.mark.usefixtures("driver")
class TestBuild:
    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login(USERS["user1"]["username"], USERS["user1"]["password"])
        sidebar = Sidebar(driver)
        sidebar.go_to_build()
        yield
        # No explicit teardown needed

    def test_agent_name_updates_progress(self, driver):
        build = BuildPage(driver)
        initial_progress = build.get_progress_text()
        build.set_agent_name("Smoke Agent")
        after_progress = build.get_progress_text()
        assert initial_progress != after_progress

    def test_framework_selection_shows_panels(self, driver):
        build = BuildPage(driver)
        build.select_framework("Selenium")
        assert build.panels_for_framework_visible()

    def test_build_blocked_without_agent_name(self, driver):
        build = BuildPage(driver)
        # Ensure field is empty
        build.type(BuildPage.AGENT_NAME_INPUT, "")
        assert not build.is_build_agent_enabled()