import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import yaml
import os

@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver(config):
    options = webdriver.ChromeOptions()
    # headless mode for CI, can be overridden via config
    if config.get("headless", True):
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config.get("implicit_wait", 5))
    yield driver
    driver.quit()