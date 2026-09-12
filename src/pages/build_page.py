from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = "[data-testid='agent-name']"
    FRAMEWORK_SELECT = "[data-testid='framework-select']"
    BUILD_AGENT_BTN = "[data-testid='build-agent']"
    PROGRESS_INDICATOR = "[data-testid='setup-progress']"

    def open_build_via_sidebar(self):
        # Assumes the user is already on dashboard; click the sidebar link
        self.click(By.CSS_SELECTOR, "[data-testid='nav-build']")

    def set_agent_name(self, name):
        self.type(By.CSS_SELECTOR, self.AGENT_NAME, name)

    def get_agent_name_status(self):
        # Assuming the status is reflected via a class or attribute; here we just check presence
        return self.is_displayed(By.CSS_SELECTOR, self.AGENT_NAME)

    def select_framework(self, framework_name):
        dropdown = self.find(By.CSS_SELECTOR, self.FRAMEWORK_SELECT)
        dropdown.click()
        # Options are assumed to have data-testid like 'framework-option-{name}'
        option_locator = f"[data-testid='framework-option-{framework_name.lower()}']"
        self.click(By.CSS_SELECTOR, option_locator)

    def get_framework_panel_visible(self, framework_name):
        panel_locator = f"[data-testid='framework-{framework_name.lower()}-panel']"
        return self.is_displayed(By.CSS_SELECTOR, panel_locator)

    def click_build_agent(self):
        self.click(By.CSS_SELECTOR, self.BUILD_AGENT_BTN)

    def is_build_agent_enabled(self):
        btn = self.find(By.CSS_SELECTOR, self.BUILD_AGENT_BTN)
        return btn.is_enabled()

    def get_progress_text(self):
        return self.get_text(By.CSS_SELECTOR, self.PROGRESS_INDICATOR)