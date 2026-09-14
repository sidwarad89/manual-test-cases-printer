import pytest
from src.pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
def test_home_page_heading_is_correct(driver):
    """
    SCRUM-1: Verify that the home page heading displays the expected text.
    """
    page = HomePage(driver)
    page.open()
    heading = page.get_heading_text()
    assert heading == "Example Domain", f"Expected heading to be 'Example Domain' but got '{heading}'"