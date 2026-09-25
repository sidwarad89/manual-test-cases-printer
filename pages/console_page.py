from selenium.webdriver.common.by import By
from .base_page import BasePage

class ConsolePage(BasePage):
    # Sidebar navigation items
    NAV_MYSPACE = (By.CSS_SELECTOR, '[data-testid="nav-myspace"]')
    NAV_BUILD = (By.CSS_SELECTOR, '[data-testid="nav-build"]')
    NAV_AGENTS = (By.CSS_SELECTOR, '[data-testid="nav-agents"]')
    NAV_MCP = (By.CSS_SELECTOR, '[data-testid="nav-mcp"]')
    NAV_ANALYTICS = (By.CSS_SELECTOR, '[data-testid="nav-analytics"]')
    NAV_SUPPORT = (By.CSS_SELECTOR, '[data-testid="nav-support"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-testid="logout"]')

    def is_sidebar_visible(self):
        # Presence of any sidebar item implies sidebar is loaded
        return self.is_visible(self.NAV_BUILD)