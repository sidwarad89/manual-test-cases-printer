import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from src.config import BASE_URL

def pytest_configure(config):
    # Register custom markers
    config.addinivalue_line("markers", "browser(name): specify browser (chrome, firefox, edge)")
    config.addinivalue_line("markers", "incognito: run test in incognito mode")
    config.addinivalue_line("markers", "mobile: simulate mobile viewport")
    config.addinivalue_line("markers", "disable_js: disable JavaScript")
    config.addinivalue_line("markers", "skip_ci: skip test in CI environment")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.node.get_closest_marker("browser")
    browser_name = browser.args[0].lower() if browser else "chrome"

    incognito = request.node.get_closest_marker("incognito")
    mobile = request.node.get_closest_marker("mobile")
    disable_js = request.node.get_closest_marker("disable_js")

    if browser_name == "chrome":
        options = ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
        if mobile:
            options.add_argument("--window-size=320,640")
        if disable_js:
            options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if incognito:
            options.set_preference("browser.privatebrowsing.autostart", True)
        if mobile:
            options.add_argument("--width=320")
            options.add_argument("--height=640")
        if disable_js:
            options.set_preference("javascript.enabled", False)
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        if incognito:
            options.add_argument("-inprivate")
        if mobile:
            options.add_argument("--window-size=320,640")
        if disable_js:
            options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    yield driver
    driver.quit()