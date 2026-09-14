import pytest
import time
from src.pages.login_page import LoginPage

@pytest.mark.browser("chrome")
def test_tc014_page_load_performance(driver):
    start = time.time()
    driver.get(driver.current_url)  # reload login page
    end = time.time()
    load_time = end - start
    assert load_time < 2.0  # seconds