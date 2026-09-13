from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    SIDEBAR = (By.ID, "sidebar")
    MY_SPACE = (By.LINK_TEXT, "My Space")
    BUILD = (By.LINK_TEXT, "Build")
    AGENTS = (By.LINK_TEXT, "Agents")
    MCP_TOOLS = (By.LINK_TEXT, "MCP Tools")
    ANALYTICS = (By.LINK_TEXT, "Analytics")
    SUPPORT = (By.LINK_TEXT, "Support")
    PROFILE_MENU = (By.ID, "profile-menu")
    LOGOUT = (By.ID, "logout")

    def sidebar_items_visible(self):
        items = [self.MY_SPACE, self.BUILD, self.AGENTS, self.MCP_TOOLS]
        return all(self.is_displayed(item) for item in items)

    def click_sidebar(self, locator):
        self.click(locator)

    def logout