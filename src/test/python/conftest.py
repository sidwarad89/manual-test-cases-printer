import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    """Create a single WebDriver instance for the whole test session."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # Run headless in CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()