# Android Selenium POM Framework (Python)

This repository contains a minimal **Page Object Model (POM)** framework for automating Android native applications using **Selenium/Appium** with Python.

## Project Layout

project-root/
├── src/
│   ├── main/python/pages/
│   │   ├── BasePage.py
│   │   └── LoginPage.py
│   └── test/python/tests/
│       ├── BaseTest.py
│       └── LoginTest.py
├── src/test/resources/
│   └── testdata.json
├── requirements.txt
├── pom.xml
├── README.md
└── .github/workflows/run-tests.yml

## How to Run Locally

1. Install dependencies  

   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt

2. Make sure **Appium Server** is running and the Android device/emulator is connected.

3. Execute the tests  

   pytest src/test/python/tests

## CI

GitHub Actions workflow is defined in `.github/workflows/run-tests.yml`.  
It installs dependencies, starts a virtual X server, records the UI with `ffmpeg`, runs the tests, and uploads the video + any test reports as artifacts.