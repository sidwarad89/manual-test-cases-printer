import json
import os
import unittest
from .BaseTest import BaseTest
from src.main.python.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class LoginTest(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Load test data (username/password) from resources
        testdata_path = os.path.join(os.path.dirname(__file__), "..", "..", "resources", "testdata.json")
        with open(testdata_path, "r") as f:
            cls.testdata = json.load(f)

    def test_valid_login_redirects_to_dashboard(self):
        """
        Verify that a valid login navigates to the dashboard screen.
        The assertion checks for an element that only exists on the dashboard.
        """
        login_page = LoginPage(self.driver)

        user = self.testdata["valid_user"]["username"]
        pwd  = self.testdata["valid_user"]["password"]
        login_page.login(user, pwd)

        # Example dashboard verification – replace with a real locator
        DASHBOARD_TITLE = (By.ID, "com.example.app:id/dashboardTitle")
        dashboard_elem = login_page.find(DASHBOARD_TITLE)
        self.assertTrue(dashboard_elem.is_displayed(),
                        msg="Dashboard title not displayed after login")