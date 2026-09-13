import pytest
from src.pages.login_page import LoginPage
from src.pages.profile_page import ProfilePage

def test_tc_qap_011_feedback_submission(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Demo_Run", "Waradss8997@")
    profile = ProfilePage(driver)
    profile.open()
    message = "Great platform!"
    profile.submit_feedback(message)
    # Verify message appears in list
    feedback_list = profile.get_latest_feedback()
    assert message in feedback_list