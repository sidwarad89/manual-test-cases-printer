import pytest
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from pages.build_page import BuildPage

@pytest.mark.usefixtures("driver", "config")
class TestBuild:
    @pytest.fixture(autouse=True)
    def login_and_navigate(self, driver, config):
        self.login_page = LoginPage(driver)
        self.sidebar = Sidebar(driver)
        self.build_page = BuildPage(driver)
        self.base_url = config["base_url"]
        self.user = config["users"]["user1"]
        # Login
        self.login_page.open(self.base_url)
        self.login_page.dismiss_welcome()
        self.login_page.login(self.user["username"], self.user["password"])
        # Navigate to Build
        self.sidebar.go_to_build()

    def test_agent_name_updates_progress(self):
        self.build_page.set_agent_name("Smoke Agent")
        progress = self.build_page.get_progress_text()
        assert "Agent Name" in progress and "complete" in progress.lower()

    def test_framework_selection_shows_sample(self):
        self.build_page.select_framework("Selenium")
        # Assume sample panel has data-testid='framework-sample'
        SAMPLE = (By.CSS_SELECTOR, "[data-testid='framework-sample']")
        assert self.build_page.is_displayed(SAMPLE)