import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver():
    headless_env = os.getenv("HEADLESS", "false").lower()
    headless = headless_env in ("true", "1", "yes")
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    # Disable sandbox and GPU for CI stability
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    # Set window size as required
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    # Cleanup
    driver.quit()