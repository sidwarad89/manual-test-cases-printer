package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.ReceiptPage;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑03 – No printer paired – attempt to print
 */
public class SCRUM1TC03Test extends BaseTest {

    @Test
    public void noPrinterPairedAttemptToPrint() {
        HomePage home = new HomePage(driver);
        home.open();

        ReceiptPage receipt = new ReceiptPage(driver);
        receipt.triggerPrint();

        Assert.assertTrue(receipt.isNoPrinterMessageDisplayed(),
                "Message 'No printer connected' should be displayed.");

        // Verify that a Connect Now button is present
        receipt.clickReconnectNow(); // just ensures the button exists; no further action needed.
    }
}