# Selenium POM Python Project

This repository contains a minimal Selenium test automation framework using the Page Object Model (POM) pattern in Python.

## Project Structure
project-root/
├── src/
│   ├── config.py          # Global configuration (e.g., base URL)
│   └── pages/
│       └── home_page.py   # Example page object
├── tests/
│   └── test_task1.py      # Example test case (SCRUM-1)
├── requirements.txt       # Python dependencies
├── conftest.py            # Pytest fixtures (WebDriver setup/teardown)
└── .github/
    └── workflows/
        └── run-tests.yml # GitHub Actions CI workflow

## Running Locally
1. Install Python 3.11+ and ensure `pip` is available.
2. Install dependencies:
   pip install -r requirements.txt
3. Execute the tests:
   pytest tests/

The tests will launch Chrome (managed automatically by Selenium Manager) and run against `https://example.com`.

## CI
GitHub Actions automatically runs the test suite on each push, records a video of the test run using Xvfb and ffmpeg, and uploads the video as an artifact.