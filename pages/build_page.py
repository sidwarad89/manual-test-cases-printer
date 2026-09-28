from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT_BTN = (By.CSS_SELECTOR, '[data-testid="build-agent"]')

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        dropdown = self.find(self.FRAMEWORK_SELECT)
        dropdown.click()
        # Assuming options are rendered as <option> elements with visible text
        option_locator = (By.XPATH, f"//option[normalize-space()='{framework_name}']")
        self.click(option_locator)

    def is_build_button_enabled(self):
        button = self.find(self.BUILD_AGENT_BTN)
        return button.is_enabled()