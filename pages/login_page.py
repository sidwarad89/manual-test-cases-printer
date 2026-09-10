```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Represent the login page."""

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, "div.alert-danger")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def enter_username(self, username: str):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def login_as(self, username: str, password: str):
        """Convenience method to perform a full login flow."""
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    def get_error_message(self) -> str:
        """Return the text of the error alert (if displayed)."""
        if self.is_displayed(self.ERROR_MSG):
            element = self.find(self.ERROR_MSG)
            return element.text
        return ""
```

---  