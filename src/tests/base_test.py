import pytest
from appium import webdriver
import os


@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": os.getenv("ANDROID_DEVICE_NAME", "Android Emulator"),
        "appPackage": os.getenv("APP_PACKAGE", "com.example.pos"),
        "appActivity": os.getenv("APP_ACTIVITY", ".MainActivity"),
        "noReset": True,
        "newCommandTimeout": 300
    }
    # Appium server URL – default to localhost
    server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
    driver = webdriver.Remote(server_url, desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()