# Printer POS Automation

Automated UI test suite for the POS application that interacts with Bluetooth thermal printers.  
The project uses **Selenium WebDriver** with **TestNG** and follows the Page Object Model (POM) pattern.

## Project structure

project-root/
├── src/
│   ├── main/java/com/example/pages/
│   │   ├── BasePage.java
│   │   ├── HomePage.java
│   │   ├── PrinterDiscoveryPage.java
│   │   ├── PrinterConnectionPage.java
│   │   ├── ReceiptPage.java
│   │   └── SettingsPage.java
│   └── test/java/com/example/tests/
│       ├── BaseTest.java
│       ├── SCRUM1TC01Test.java
│       ├── ... (one class per test case)
│       └── SCRUM1TC20Test.java
├── src/test/resources/
│   └── testdata.json
├── pom.xml
└── .github/workflows/run-tests.yml

## Prerequisites

- JDK 17+
- Maven 3.9+
- Chrome browser + matching ChromeDriver (automatically resolved by Selenium Manager)

## Running the tests locally

mvn clean test

## CI

A GitHub Actions workflow (`.github/workflows/run-tests.yml`) runs the full suite on every push.

---

Enjoy testing! 🚀