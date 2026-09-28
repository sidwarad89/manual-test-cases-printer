from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT = (By.CSS_SELECTOR, '[data-testid="build-agent"]')

    def enter_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        # Assuming it's a standard <select> element; we click and send keys
        self.click(self.FRAMEWORK_SELECT)
        self.type(self.FRAMEWORK_SELECT, framework_name)

    def is_build_enabled(self):
        attr = self.get_attribute(self.BUILD_AGENT, "disabled")
        return attr is None  # If no disabled attribute, button is enabled