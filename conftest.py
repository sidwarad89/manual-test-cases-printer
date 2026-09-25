import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    headless_env = os.getenv("HEADLESS", "false").lower()
    headless = headless_env == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    # Disable GPU and set window size for consistency in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-agent-platform.com"