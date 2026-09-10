```python
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver", "logger")
class TestLogin:
    """Test suite for login functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Navigate to the base URL before each test."""
        self.base_url = "https://example.com"      # <‑‑ CHANGE TO YOUR AUT
        driver.get(self.base_url)
        self.logger = logger
        self.driver = driver
        self.home = HomePage(driver, logger)
        self.login = LoginPage(driver, logger)

    def test_successful_login(self):
        """Valid credentials should log the user in and land on the dashboard."""
        self.home.click_login()
        self.login.login_as("valid_user", "valid_password")
        # Example assertion – adapt to what your app shows after login
        assert "Dashboard" in self.driver.title, "Dashboard title not found after login"

    def test_invalid_login_shows_error(self):
        """Invalid credentials must display an appropriate error message."""
        self.home.click_login()
        self.login.login_as("invalid_user", "wrong_password")
        error_msg = self.login.get_error_message()
        assert error_msg, "Expected an error message but none was displayed"
        assert "Invalid username or password" in error_msg

    @pytest.mark.parametrize(
        "username,password",
        [
            ("", "somepass"),          # missing username
            ("someuser", ""),          # missing password
            ("", ""),                  # both missing
        ],
    )
    def test_login_validation(self, username, password):
        """Empty fields should be validated by the UI."""
        self.home.click_login()
        self.login.login_as(username, password)
        # Assuming the app shows the same generic error for empty fields
        error_msg = self.login.get_error_message()
        assert error_msg, "Validation error expected for empty fields"
        assert "required" in error_msg.lower()
```

---  

### How to run

1. **Create the project folder** and place each file in the path shown by its marker comment.  
2. Install dependencies:

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Execute the tests with pytest:

```bash
pytest -s -v
```

* `-s` shows the logger output in the console.  
* Adjust the `self.base_url` and the locators inside the page classes to match your actual application under test (AUT).  

You now have a clean POM‑based Selenium test framework ready for additional test cases. Happy testing!