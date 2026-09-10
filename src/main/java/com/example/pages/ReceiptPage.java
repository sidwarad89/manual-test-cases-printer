package com.example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Page dealing with receipt generation and printing.
 */
public class ReceiptPage extends BasePage {

    private By printReceiptBtn = By.id("print-receipt");
    private By reconnectNowBtn = By.id("reconnect-now");
    private By noPrinterMsg = By.id("no-printer-message");
    private By duplicateWatermark = By.id("duplicate-watermark");
    private By printerErrorMsg = By.id("printer-error");
    private By supervisorPinInput = By.id("supervisor-pin");
    private By supervisorConfirmBtn = By.id("supervisor-confirm");

    public ReceiptPage(WebDriver driver) {
        super(driver);
    }

    public void triggerPrint() {
        driver.findElement(printReceiptBtn).click();
    }

    public boolean isNoPrinterMessageDisplayed() {
        return driver.findElements(noPrinterMsg).size() > 0;
    }

    public void clickReconnectNow() {
        driver.findElement(reconnectNowBtn).click();
    }

    public boolean isDuplicateWatermarkDisplayed() {
        return driver.findElements(duplicateWatermark).size() > 0;
    }

    public String getPrinterErrorMessage() {
        if (driver.findElements(printerErrorMsg).size() > 0) {
            return driver.findElement(printerErrorMsg).getText();
        }
        return "";
    }

    public void enterSupervisorPin(String pin) {
        driver.findElement(supervisorPinInput).sendKeys(pin);
        driver.findElement(supervisorConfirmBtn).click();
    }
}