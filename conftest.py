import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    # disable GPU and sandbox for CI stability
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # avoid detection
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(0)  # rely on explicit waits only
    yield driver
    driver.quit()