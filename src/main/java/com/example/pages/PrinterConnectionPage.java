package com.example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Handles the connection flow after a printer is selected.
 */
public class PrinterConnectionPage extends BasePage {

    private By connectBtn = By.id("confirm-connect");
    private By statusLabel = By.id("connection-status");
    private By errorMsg = By.id("connection-error");

    public PrinterConnectionPage(WebDriver driver) {
        super(driver);
    }

    public void confirmConnection() {
        driver.findElement(connectBtn).click();
    }

    public String getConnectionStatus() {
        return driver.findElement(statusLabel).getText();
    }

    public String getErrorMessage() {
        return driver.findElement(errorMsg).getText();
    }
}