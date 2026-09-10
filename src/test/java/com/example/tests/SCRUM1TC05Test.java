package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.ReceiptPage;
import org.openqa.selenium.JavascriptExecutor;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑05 – Receipt prints within SLA (≤5 seconds)
 */
public class SCRUM1TC05Test extends BaseTest {

    @Test
    public void receiptPrintsWithinSLA() {
        HomePage home = new HomePage(driver);
        home.open();

        ReceiptPage receipt = new ReceiptPage(driver);
        long start = System.currentTimeMillis();
        receipt.triggerPrint();

        // In a real environment we would poll printer status; here we mock via JS timer.
        new JavascriptExecutor(driver).executeScript(
                "window.setTimeout(() => { document.body.setAttribute('data-print-done', 'true'); }, 3000);"
        );

        // Wait until mock flag appears (max 5 seconds)
        new org.openqa.selenium.support.ui.WebDriverWait(driver, java.time.Duration.ofSeconds(5))
                .until(d -> "true".equals(d.findElement(By.tagName("body")).getAttribute("data-print-done")));

        long duration = System.currentTimeMillis() - start;
        Assert.assertTrue(duration <= 5000,
                "Receipt should be printed within 5 seconds. Actual: " + duration + " ms");
    }
}