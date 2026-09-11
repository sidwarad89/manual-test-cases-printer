from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME_INPUT = (By.CSS_SELECTOR, '[data-testid="agent-name"]')
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, '[data-testid="framework-select"]')
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, '[data-testid="build-agent"]')
    PROGRESS_INDICATOR = (By.CSS_SELECTOR, '[data-testid="setup-progress"]')
    # Assuming progress indicator contains text like "2/5 completed"
    SAMPLE_PANEL = (By.CSS_SELECTOR, '[data-testid="sample-code"]')
    PREREQ_PANEL = (By.CSS_SELECTOR, '[data-testid="prerequisites"]')

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME_INPUT, name)

    def get_progress_text(self):
        return self.get_text(self.PROGRESS_INDICATOR)

    def select_framework(self, framework_name):
        # Assuming a standard <select> element; use visible text
        from selenium.webdriver.support.ui import Select
        select_elem = self.find(self.FRAMEWORK_SELECT)
        Select(select_elem).select_by_visible_text(framework_name)

    def is_build_agent_enabled(self):
        try:
            btn = self.find(self.BUILD_AGENT_BUTTON)
            return btn.is_enabled()
        except:
            return False

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BUTTON)

    def panels_for_framework_visible(self):
        sample_visible = self.is_displayed(self.SAMPLE_PANEL)
        prereq_visible = self.is_displayed(self.PREREQ_PANEL)
        return sample_visible and prereq_visible