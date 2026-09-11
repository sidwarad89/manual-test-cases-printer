import json
import os
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

# Load capabilities from JSON files
def load_caps(platform: str):
    caps_path = os.path.join(os.path.dirname(__file__), "capabilities", f"{platform}.json")
    with open(caps_path) as f:
        return json.load(f)

ANDROID_CAPS = load_caps("android")
IOS_CAPS = load_caps("ios")

@pytest.fixture(params=["android", "ios"])
def driver(request):
    platform = request.param
    caps = ANDROID_CAPS if platform == "android" else IOS_CAPS

    # Initialize Appium Options and load capabilities
    options = AppiumOptions()
    options.load_capabilities(caps)

    # Assuming Appium server is running locally; adjust URL if needed
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    driver.implicitly_wait(10)  # default implicit wait

    yield driver

    driver.quit()