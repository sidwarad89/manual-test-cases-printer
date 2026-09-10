```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Represent the home (landing) page."""

    # Example locators – adapt to your application
    LOGO = (By.ID, "site-logo")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    WELCOME_BANNER = (By.CSS_SELECTOR, "div.welcome")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def is_logo_visible(self) -> bool:
        return self.is_displayed(self.LOGO)

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def get_welcome_text(self) -> str:
        element = self.find(self.WELCOME_BANNER)
        return element.text
```

---  