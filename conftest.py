import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture
def driver():
    options = Options()
    # Do NOT set headless to allow video capture
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()