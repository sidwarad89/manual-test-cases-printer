from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class BuildPage(BasePage):
    AGENT_NAME = (By.CSS_SELECTOR, "[data-testid=agent-name]")
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, "[data-testid=framework-select]")
    BUILD_AGENT_BUTTON = (By.CSS_SELECTOR, "[data-testid=build-agent]")
    # Assuming a generic progress count element
    PROGRESS_COUNT = (By.CSS_SELECTOR, "[data-testid=setup-progress-count]")

    def set_agent_name(self, name):
        self.send_keys(self.AGENT_NAME, name)

    def get_agent_name_value(self):
        return self.get_attribute(self.AGENT_NAME, "value")

    def select_framework(self, framework_name):
        select_elem = self.find(self.FRAMEWORK_SELECT)
        for option in select_elem.find_elements(By.TAG_NAME, "option"):
            if option.text.strip().lower() == framework_name.lower():
                option.click()
                break

    def get_selected_framework(self):
        select_elem = self.find(self.FRAMEWORK_SELECT)
        for option in select_elem.find_elements(By.TAG_NAME, "option"):
            if option.is_selected():
                return option.text.strip()
        return ""

    def is_build_agent_enabled(self):
        try:
            button = self.find(self.BUILD_AGENT_BUTTON)
            disabled = button.get_attribute("disabled")
            return disabled is None
        except:
            return False

    def click_build_agent(self):
        self.click(self.BUILD_AGENT_BUTTON)

    def get_progress_count(self):
        if self.is_visible(self.PROGRESS_COUNT):
            return self.find(self.PROGRESS_COUNT).text
        return None