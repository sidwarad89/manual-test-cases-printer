import pytest
import yaml
from appium import webdriver
from pathlib import Path
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.fixture(scope="session")
def driver():
    # Load configuration
    config_path = Path(__file__).parents[2] / "config.yaml"
    with open(config_path) as f:
        caps = yaml.safe_load(f)

    # Appium server URL – adjust if needed
    appium_server = "http://localhost:4723/wd/hub"

    driver = webdriver.Remote(command_executor=appium_server, desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture
def printer_page(driver):
    return PrinterPage(driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)