from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, '[data-testid="build-agent"]')
    PROGRESS_INDICATOR = (By.CSS_SELECTOR, '[data-testid="setup-progress"]')
    SAMPLE_PANEL = (By.CSS_SELECTOR, '[data-testid="sample-panel"]')
    PREREQ_PANEL = (By.CSS_SELECTOR, '[data-testid="prereq-panel"]')

    def enter_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        dropdown = self.find(self.FRAMEWORK_SELECT)
        dropdown.click()
        option_locator = (By.XPATH, f"//option[normalize-space(.)='{framework_name}']")
        self.click(option_locator)

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BUTTON)

    def is_build_agent_enabled(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.BUILD_AGENT_BUTTON))
            return button.is_enabled()
        except:
            return False

    def get_progress_text(self):
        return self.get_text(self.PROGRESS_INDICATOR)

    def is_sample_visible(self):
        return self.is_visible(self.SAMPLE_PANEL)

    def is_prereq_visible(self):
        return self.is_visible(self.PREREQ_PANEL)