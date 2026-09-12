from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class DashboardPage(BasePage):
    NAV_BUILD = "[data-testid='nav-build']"
    NAV_MYSPACE = "[data-testid='nav-myspace']"
    NAV_AGENTS = "[data-testid='nav-agents']"
    NAV_MCP = "[data-testid='nav-mcp']"
    NAV_ANALYTICS = "[data-testid='nav-analytics']"
    NAV_SUPPORT = "[data-testid='nav-support']"
    LOGOUT = "[data-testid='logout']"

    def go_to_build(self):
        self.click(By.CSS_SELECTOR, self.NAV_BUILD)

    def go_to_myspace(self):
        self.click(By.CSS_SELECTOR, self.NAV_MYSPACE)

    def go_to_agents(self):
        self.click(By.CSS_SELECTOR, self.NAV_AGENTS)

    def go_to_mcp(self):
        self.click(By.CSS_SELECTOR, self.NAV_MCP)

    def go_to_analytics(self):
        self.click(By.CSS_SELECTOR, self.NAV_ANALYTICS)

    def go_to_support(self):
        self.click(By.CSS_SELECTOR, self.NAV_SUPPORT)

    def logout(self):
        self.click(By.CSS_SELECTOR, self.LOGOUT)