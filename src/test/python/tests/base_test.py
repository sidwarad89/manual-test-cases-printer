import os
import unittest
from appium import webdriver
from typing import Dict

class BaseTest(unittest.TestCase):
    """Base test class that sets up and tears down the Appium driver."""

    driver = None

    @classmethod
    def setUpClass(cls):
        """Create a new Appium driver instance for Android."""
        # Desired capabilities – replace placeholder values with real ones.
        desired_caps: Dict[str, str] = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "automationName": "UiAutomator2",
            # The following must match the APK under test.
            "appPackage": "com.example.printer",
            "appActivity": ".MainActivity",
            "noReset": True,
            "newCommandTimeout": 300
        }

        # Appium server URL – typically http://localhost:4723/wd/hub
        appium_server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
        cls.driver = webdriver.Remote(appium_server, desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        """Quit the driver after all tests have run."""
        if cls.driver:
            cls.driver.quit()