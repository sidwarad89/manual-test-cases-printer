from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class BuildPage(BasePage):
    NAV_BUILD = (By.CSS_SELECTOR, "[data-testid='nav-build']")
    AGENT_NAME_INPUT = (By.CSS_SELECTOR, "[data-testid='agent-name']")
    FRAMEWORK_SELECT = (By.CSS_SELECTOR, "[data-testid='framework-select']")
    BUILD_AGENT_BTN = (By.CSS_SELECTOR, "[data-testid='build-agent']")
    SETUP_PROGRESS = (By.CSS_SELECTOR, "[data-testid='setup-progress']")  # assumed

    def navigate(self):
        self.click(self.NAV_BUILD)

    def set_agent_name(self, name):
        self.type(self.AGENT_NAME_INPUT, name)

    def select_framework(self, framework_name):
        select_elem = self.find(self.FRAMEWORK_SELECT)
        # simple click approach; assumes options are clickable items inside the select
        option = select_elem.find_element(By.XPATH, f".//option[normalize-space()='{framework_name}']")
        option.click()

    def is_build_enabled(self):
        try:
            btn = self.find(self.BUILD_AGENT_BTN)
            return btn.is_enabled()
        except:
            return False

    def click_build(self):
        self.click(self.BUILD_AGENT_BTN)

    def get_setup_progress_text(self):
        return self.find(self.SETUP_PROGRESS).text