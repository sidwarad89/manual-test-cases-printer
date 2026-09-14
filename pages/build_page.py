from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, "[data-testid='agent-name']")
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, "[data-testid='framework-select']")
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, "[data-testid='build-agent']")
    PROGRESS_INDICATOR = (By.CSS_SELECTOR, "[data-testid='setup-progress']")  # hypothetical

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME, name)

    def select_framework(self, framework_name):
        # Assuming it's a <select> element; Selenium can select by visible text
        from selenium.webdriver.support.ui import Select
        elem = self.find(self.FRAMEWORK_SELECT)
        select = Select(elem)
        select.select_by_visible_text(framework_name)

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BUTTON)

    def is_build_agent_enabled(self):
        button = self.find(self.BUILD_AGENT_BUTTON)
        return button.is_enabled()

    def get_progress_text(self):
        return self.find(self.PROGRESS_INDICATOR).text