import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    options = Options()
    # No headless to allow video capture
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Disable infobars and extensions for stability
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    # Set a reasonable window size (Xvfb will provide virtual display)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()