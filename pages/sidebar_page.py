from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SidebarPage(BasePage):
    NAV_MYSPACE = (By.CSS_SELECTOR, "[data-testid=nav-myspace]")
    NAV_AGENTS = (By.CSS_SELECTOR, "[data-testid=nav-agents]")
    NAV_MCP = (By.CSS_SELECTOR, "[data-testid=nav-mcp]")
    NAV_ANALYTICS = (By.CSS_SELECTOR, "[data-testid=nav-analytics]")
    NAV_SUPPORT = (By.CSS_SELECTOR, "[data-testid=nav-support]")
    NAV_BUILD = (By.CSS_SELECTOR, "[data-testid=nav-build]")
    LOGOUT = (By.CSS_SELECTOR, "[data-testid=logout]")

    def click_myspace(self):
        self.click(self.NAV_MYSPACE)

    def click_agents(self):
        self.click(self.NAV_AGENTS)

    def click_mcp(self):
        self.click(self.NAV_MCP)

    def click_analytics(self):
        self.click(self.NAV_ANALYTICS)

    def click_support(self):
        self.click(self.NAV_SUPPORT)

    def click_build(self):
        self.click(self.NAV_BUILD)

    def click_logout(self):
        self.click(self.LOGOUT)