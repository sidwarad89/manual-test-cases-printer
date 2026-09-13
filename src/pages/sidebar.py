from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class Sidebar(BasePage):
    MYSPACE = (By.CSS_SELECTOR, "[data-testid='nav-myspace']")
    AGENTS = (By.CSS_SELECTOR, "[data-testid='nav-agents']")
    MCP = (By.CSS_SELECTOR, "[data-testid='nav-mcp']")
    ANALYTICS = (By.CSS_SELECTOR, "[data-testid='nav-analytics']")
    SUPPORT = (By.CSS_SELECTOR, "[data-testid='nav-support']")

    def go_to_myspace(self):
        self.click(self.MYSPACE)

    def go_to_agents(self):
        self.click(self.AGENTS)

    def go_to_mcp(self):
        self.click(self.MCP)

    def go_to_analytics(self):
        self.click(self.ANALYTICS)

    def go_to_support(self):
        self.click(self.SUPPORT)