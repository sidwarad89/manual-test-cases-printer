package com.example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Represents the main screen of the POS web application.
 */
public class HomePage extends BasePage {

    private By connectPrinterBtn = By.id("connect-printer");
    private By logoutBtn = By.id("logout");

    public HomePage(WebDriver driver) {
        super(driver);
    }

    public void open() {
        navigateTo("https://example-pos-app.com");
    }

    public PrinterDiscoveryPage goToPrinterDiscovery() {
        driver.findElement(connectPrinterBtn).click();
        return new PrinterDiscoveryPage(driver);
    }

    public SettingsPage goToSettings() {
        driver.findElement(logoutBtn).click();
        return new SettingsPage(driver);
    }
}