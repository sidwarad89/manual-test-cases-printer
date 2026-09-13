from selenium.webdriver.common.by import By
from .base_page import BasePage

class SidebarPage(BasePage):
    MY_SPACE = (By.CSS_SELECTOR, '[data-testid="nav-myspace"]')
    AGENTS = (By.CSS_SELECTOR, '[data-testid="nav-agents"]')
    MCP_TOOLS = (By.CSS_SELECTOR, '[data-testid="nav-mcp"]')
    ANALYTICS = (By.CSS_SELECTOR, '[data-testid="nav-analytics"]')
    SUPPORT = (By.CSS_SELECTOR, '[data-testid="nav-support"]')
    LOGOUT = (By.CSS_SELECTOR, '[data-testid="logout"]')
    PROFILE_MENU = (By.CSS_SELECTOR, '[data-testid="profile-menu"]')  # hypothetical

    def click_myspace(self):
        self.click(self.MY_SPACE)

    def click_agents(self):
        self.click(self.AGENTS)

    def click_mcp_tools(self):
        self.click(self.MCP_TOOLS)

    def click_analytics(self):
        self.click(self.ANALYTICS)

    def click_support(self):
        self.click(self.SUPPORT)

    def open_profile_menu(self):
        self.click(self.PROFILE_MENU)

    def logout(self):
        self.click(self.LOGOUT)