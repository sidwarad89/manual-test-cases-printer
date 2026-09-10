"""Pytest fixtures for Selenium WebDriver setup and teardown."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Create a new Chrome WebDriver instance for each test function."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # Run in headless mode for CI
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    # Initialize driver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()