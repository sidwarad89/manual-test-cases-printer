from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, '[data-testid="build-agent"]')

    def enter_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        # Assuming the select element is a standard <select>
        select_elem = self.find(self.FRAMEWORK_SELECT)
        for option in select_elem.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == framework_name:
                option.click()
                break

    def is_build_button_enabled(self):
        return self.is_enabled(self.BUILD_AGENT_BUTTON)