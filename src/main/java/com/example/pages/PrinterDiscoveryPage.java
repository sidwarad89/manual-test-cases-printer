package com.example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import java.util.List;

/**
 * Page that lists discoverable/paired printers.
 */
public class PrinterDiscoveryPage extends BasePage {

    // Simplified locators – in a real app these would be more specific.
    private By printerListItems = By.cssSelector(".printer-list .printer-item");
    private By refreshBtn = By.id("refresh-printers");

    public PrinterDiscoveryPage(WebDriver driver) {
        super(driver);
    }

    public void refreshList() {
        driver.findElement(refreshBtn).click();
    }

    public List<WebElement> getAvailablePrinters() {
        return driver.findElements(printerListItems);
    }

    public PrinterConnectionPage selectPrinterByName(String printerName) {
        for (WebElement item : getAvailablePrinters()) {
            if (item.getText().contains(printerName)) {
                item.click();
                return new PrinterConnectionPage(driver);
            }
        }
        throw new IllegalArgumentException("Printer with name '" + printerName + "' not found in list.");
    }
}