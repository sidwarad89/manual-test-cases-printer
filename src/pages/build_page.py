from selenium.webdriver.common.by import By
from .base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME_INPUT = (By.CSS_SELECTOR, "[data-testid=agent-name]")
    SETUP_PROGRESS = (By.CSS_SELECTOR, "[data-testid=setup-progress]")
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, "[data-testid=framework-select]")
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, "[data-testid=build-agent]")

    def open_via_sidebar(self, sidebar):
        sidebar.go_to_build()

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME_INPUT, name)

    def get_progress_text(self):
        return self.get_text(self.SETUP_PROGRESS)

    def select_framework(self, framework_name):
        select_elem = self.wait_for_element(self.FRAMEWORK_SELECT)
        select_elem.click()
        option = (By.XPATH, f".//option[normalize-space()='{framework_name}']")
        self.click(option)

    def is_build_agent_enabled(self):
        btn = self.wait_for_element(self.BUILD_AGENT_BUTTON)
        return btn.is_enabled()

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BUTTON)