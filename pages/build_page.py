from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME_INPUT = (By.CSS_SELECTOR, "[data-testid=agent-name]")
    SETUP_PROGRESS = (By.CSS_SELECTOR, "[data-testid=setup-progress]")
    FRAMEWORK_DROPDOWN = (By.CSS_SELECTOR, "[data-testid=framework-select]")
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, "[data-testid=build-agent]")
    SAMPLE_PANEL = (By.CSS_SELECTOR, "[data-testid=framework-sample]")  # Assuming a panel for sample code

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME_INPUT, name)

    def get_progress_text(self):
        return self.get_text(self.SETUP_PROGRESS)

    def select_framework(self, framework_name):
        dropdown = self.find(self.FRAMEWORK_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(framework_name)

    def is_build_enabled(self):
        button = self.find(self.BUILD_AGENT_BUTTON)
        return button.is_enabled()

    def click_build(self):
        self.click(self.BUILD_AGENT_BUTTON)

    def sample_panel_visible(self):
        return self.is_displayed(self.SAMPLE_PANEL)