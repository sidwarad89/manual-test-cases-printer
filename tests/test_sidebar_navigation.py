import pytest
from pages.login_page import LoginPage
from pages.console_page import ConsolePage

NAV_ITEMS = [
    ("nav-myspace", "myspace"),
    ("nav-agents", "agents"),
    ("nav-mcp", "mcp"),
    ("nav-analytics", "analytics"),
    ("nav-support", "support")
]

def test_sidebar_navigation(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login("Demo_Run", "Waradss8997@")
    console = ConsolePage(driver)
    for testid, url_fragment in NAV_ITEMS:
        locator = (By.CSS_SELECTOR, f'[data-testid="{testid}"]')
        console.click(locator)
        current_url = console.get_current_url()
        assert url_fragment in current_url, f"URL should contain '{url_fragment}' after clicking {testid}"