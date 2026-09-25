from selenium.webdriver.common.by import By
from .base_page import BasePage

class ConsolePage(BasePage):
    NAV_BUILD = (By.CSS_SELECTOR, '[data-testid="nav-build"]')
    NAV_MYSPACE = (By.CSS_SELECTOR, '[data-testid="nav-myspace"]')
    NAV_AGENTS = (By.CSS_SELECTOR, '[data-testid="nav-agents"]')
    NAV_MCP = (By.CSS_SELECTOR, '[data-testid="nav-mcp"]')
    NAV_ANALYTICS = (By.CSS_SELECTOR, '[data-testid="nav-analytics"]')
    NAV_SUPPORT = (By.CSS_SELECTOR, '[data-testid="nav-support"]')
    LOGOUT = (By.CSS_SELECTOR, '[data-testid="logout"]')
    FEEDBACK_TEXT = (By.CSS_SELECTOR, '[data-testid="feedback-text"]')
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, '[data-testid="feedback-submit"]')

    def go_to_build(self):
        self.click(self.NAV_BUILD)

    def go_to_myspace(self):
        self.click(self.NAV_MYSPACE)

    def go_to_agents(self):
        self.click(self.NAV_AGENTS)

    def go_to_mcp(self):
        self.click(self.NAV_MCP)

    def go_to_analytics(self):
        self.click(self.NAV_ANALYTICS)

    def go_to_support(self):
        self.click(self.NAV_SUPPORT)

    def logout(self):
        self.click(self.LOGOUT)

    def submit_feedback(self, text):
        self.type(self.FEEDBACK_TEXT, text)
        self.click(self.FEEDBACK_SUBMIT)