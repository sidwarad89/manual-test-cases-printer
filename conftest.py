import os
import pytest
from appium import webdriver

@pytest.fixture(scope="session")
def driver():
    """
    Initializes the Appium driver for the mobile application under test.
    Uses environment variables for configuration.
    """
    appium_server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
    desired_caps = {
        "platformName": os.getenv("PLATFORM_NAME", "Android"),
        "platformVersion": os.getenv("PLATFORM_VERSION", "10"),
        "deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
        "automationName": os.getenv("AUTOMATION_NAME", "UiAutomator2"),
        "appPackage": os.getenv("APP_PACKAGE", "com.example.printerapp"),
        "appActivity": os.getenv("APP_ACTIVITY", ".MainActivity"),
        "noReset": True,
        "newCommandTimeout": 300,
    }

    driver = webdriver.Remote(command_executor=appium_server, desired_capabilities=desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()