import os
import unittest
import logging
from appium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base test class that handles driver setup/teardown for Android.
    """

    @classmethod
    def setUpClass(cls):
        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s")
        cls.logger = logging.getLogger(cls.__name__)

        # Desired capabilities – replace placeholders with real values
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": os.getenv("ANDROID_DEVICE_NAME", "Android Emulator"),
            "appPackage": os.getenv("ANDROID_APP_PACKAGE", "com.example.app"),
            "appActivity": os.getenv("ANDROID_APP_ACTIVITY", ".MainActivity"),
            "noReset": True,
            "newCommandTimeout": 300
        }

        # Appium server URL – default assumes local server
        appium_server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
        cls.logger.info(f"Connecting to Appium server at {appium_server} with caps: {desired_caps}")

        cls.driver = webdriver.Remote(appium_server, desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("Quitting driver")
        cls.driver.quit()