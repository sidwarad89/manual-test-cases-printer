package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.ReceiptPage;
import org.openqa.selenium.By;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑04 – Printer out of range – automatic retry
 */
public class SCRUM1TC04Test extends BaseTest {

    @Test
    public void printerOutOfRangeAutomaticRetry() {
        HomePage home = new HomePage(driver);
        home.open();

        // Simulate that printer was previously connected; now we just attempt to print.
        ReceiptPage receipt = new ReceiptPage(driver);
        receipt.triggerPrint();

        // Expected error message after retries
        String error = receipt.getPrinterErrorMessage();
        Assert.assertTrue(error.contains("Printer disconnected"),
                "Expected disconnect message after printer out of range.");

        // Ensure the UI indicates up to 3 retries (mocked via message)
        Assert.assertTrue(error.matches(".*retry\\s*\\d\\s*of\\s*3.*"),
                "Retry count up to 3 should be displayed.");
    }
}