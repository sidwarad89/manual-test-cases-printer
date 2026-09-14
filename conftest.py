import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Do NOT use headless to allow video capture
    # options.add_argument("--headless")  # intentionally omitted
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    # Navigate to base URL for convenience; individual tests can navigate elsewhere
    driver.get(BASE_URL)
    yield driver
    driver.quit()