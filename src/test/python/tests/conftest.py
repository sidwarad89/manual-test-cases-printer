"""Pytest fixtures for Selenium WebDriver."""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to initialize and quit a WebDriver instance.
    By default uses Chrome; can be overridden with a CLI option.
    """
    browser = request.config.getoption("--browser", default="chrome")
    if browser.lower() == "firefox":
        driver_instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver_instance = webdriver.Chrome(ChromeDriverManager().install())

    driver_instance.maximize_window()
    driver_instance.implicitly_wait(5)

    yield driver_instance
    driver_instance.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests against (chrome or firefox)",
    )