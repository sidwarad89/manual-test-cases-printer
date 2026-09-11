# Mobile Automation Project (Android)

This repository contains a sample Selenium/Appium test automation framework for Android using the Page Object Model (POM) pattern in Python.

## Project Structure
project-root/
├── src/
│   ├── main/
│   │   └── python/
│   │       └── pages/
│   │           ├── __init__.py
│   │           ├── base_page.py
│   │           └── printer_page.py
│   └── test/
│       └── python/
│           └── tests/
│               ├── __init__.py
│               ├── base_test.py
│               ├── test_printer.py
│               └── test_printer_flow.py
├── src/test/resources/
│   └── testdata.json
├── requirements.txt
├── .github/workflows/run-tests.yml
└── README.md

## How to Run Locally
1. Install dependencies  
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Make sure an Android device/emulator is available and the `appPackage` / `appActivity` in `BaseTest` are set correctly.

3. Execute the tests  
   pytest src/test/python/tests

## CI
GitHub Actions workflow (`.github/workflows/run-tests.yml`) runs the tests on every push, records the UI with `ffmpeg`, and uploads the video and any test reports as artifacts.