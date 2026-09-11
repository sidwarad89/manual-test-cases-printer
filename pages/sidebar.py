from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Sidebar(BasePage):
    NAV_BUILD = (By.CSS_SELECTOR, '[data-testid="nav-build"]')
    NAV_MYSPACE = (By.CSS_SELECTOR, '[data-testid="nav-myspace"]')
    NAV_AGENTS = (By.CSS_SELECTOR, '[data-testid="nav-agents"]')
    NAV_MCP = (By.CSS_SELECTOR, '[data-testid="nav-mcp"]')
    NAV_ANALYTICS = (By.CSS_SELECTOR, '[data-testid="nav-analytics"]')
    NAV_SUPPORT = (By.CSS_SELECTOR, '[data-testid="nav-support"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-testid="logout"]')

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
        self.click(self.LOGOUT_BUTTON)