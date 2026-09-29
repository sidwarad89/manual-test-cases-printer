from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class ProfilePage(BasePage):
    FEEDBACK_TEXT = (By.CSS_SELECTOR, "[data-testid=feedback-text]")
    FEEDBACK_SUBMIT = (By.CSS_SELECTOR, "[data-testid=feedback-submit]")
    FEEDBACK_ITEMS = (By.CSS_SELECTOR, "[data-testid=feedback-item]") 