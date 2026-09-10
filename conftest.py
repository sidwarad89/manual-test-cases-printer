```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger


@pytest.fixture(scope="session")
def logger():
    """Provide a logger instance for the entire test session."""
    return get_logger(__name__)


@pytest.fixture(scope="function")
def driver(request, logger):
    """
    Initialise a Chrome WebDriver instance.
    The driver is closed after each test function.
    """
    logger.info("Setting up Chrome WebDriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # Run headless; remove if you need UI
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=options)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    logger.info("WebDriver session started")
    return driver
```

---  