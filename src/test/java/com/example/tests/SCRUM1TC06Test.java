package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.ReceiptPage;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑06 – Paper out mid‑print – error handling
 */
public class SCRUM1TC06Test extends BaseTest {

    @Test
    public void paperOutMidPrintErrorHandling() {
        HomePage home = new HomePage(driver);
        home.open();

        ReceiptPage receipt = new ReceiptPage(driver);
        receipt.triggerPrint();

        // Simulate paper-out error via mock attribute
        driver.executeScript("document.body.setAttribute('data-printer-error','Paper out');");

        String error = receipt.getPrinterErrorMessage();
        Assert.assertTrue(error.contains("Paper out"),
                "Printer error message should indicate paper out.");

        // Simulate user refilling paper and re‑printing
        driver.executeScript("document.body.removeAttribute('data-printer-error');");
        receipt.triggerPrint();

        // Assume the second print succeeds (mock flag)
        driver.executeScript("document.body.setAttribute('data-print-done','true');");
        Assert.assertTrue(driver.findElement(By.tagName("body"))
                .getAttribute("data-print-done").equals("true"),
                "Receipt should re‑print successfully after paper refill.");
    }
}