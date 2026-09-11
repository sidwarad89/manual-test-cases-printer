import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Do not use headless to allow video capture in CI
    # Additional options can be set here if needed
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()