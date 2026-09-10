# POS Printer Automation Suite

This repository contains a Selenium‑based test automation framework (Python + PyTest) that validates the POS printer integration scenarios described in Jira **SCRUM‑1**.

## Project Layout

project-root/
├── requirements.txt          # Python dependencies
├── conftest.py               # PyTest fixtures (WebDriver)
├── src/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   ├── printer_list_page.py
│   │   ├── print_receipt_page.py
│   │   └── settings_page.py
│   └── tests/
│       └── test_printer_flow.py
└── .github/
    └── workflows/
        └── run-tests.yml   # GitHub Actions CI workflow

## How to Run Locally

1. Install dependencies  

   pip install -r requirements.txt

2. Execute the test suite  

   pytest -s src/tests

The tests run headlessly using Chrome; you can modify `conftest.py` to use a different browser or to run with a UI.

## CI Integration

The workflow `.github/workflows/run-tests.yml` triggers on every push to any branch, sets up Python 3.11, installs the required packages, and runs the full PyTest suite. No additional configuration is required.

--- 

Feel free to extend the