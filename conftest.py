import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    # Chrome runs in CI without a display; disable sandboxing issues
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()