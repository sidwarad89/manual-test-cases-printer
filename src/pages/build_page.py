from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    NAV_BUILD = (By.CSS_SELECTOR, '[data-testid="nav-build"]')
    AGENT_NAME = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT_BTN = (By.CSS_SELECTOR, '[data-testid="build-agent"]')
    PROGRESS_INDICATOR = (By.CSS_SELECTOR, '[data-testid="setup-progress"]')  # hypothetical

    def go_to_build(self):
        self.click(self.NAV_BUILD)

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        # Assuming it's a <select> element; using visible text via JS
        self.click(self.FRAMEWORK_SELECT)
        option_locator = (By.XPATH, f"//option[text()='{framework_name}']")
        self.click(option_locator)

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BTN)

    def is_build_agent_enabled(self):
        # Returns True if button is enabled
        element = self.find(self.BUILD_AGENT_BTN)
        return element.is_enabled()

    def get_progress_text(self):
        return self.get_text(self.PROGRESS_INDICATOR)