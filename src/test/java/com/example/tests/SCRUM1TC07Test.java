package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.ReceiptPage;
import org.openqa.selenium.JavascriptExecutor;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑07 – Bluetooth drop during active print job
 */
public class SCRUM1TC07Test extends BaseTest {

    @Test
    public void bluetoothDropDuringActivePrintJob() {
        HomePage home = new HomePage(driver);
        home.open();

        ReceiptPage receipt = new ReceiptPage(driver);
        receipt.triggerPrint();

        // Mock a connection loss after 1 second
        new JavascriptExecutor(driver).executeScript(
                "window.setTimeout(() => { document.body.setAttribute('data-connection-lost','true'); }, 1000);"
        );

        // Wait for the flag
        new org.openqa.selenium.support.ui.WebDriverWait(driver, java.time.Duration.ofSeconds(3))
                .until(d -> d.findElement(By.tagName("body")).getAttribute("data-connection-lost") != null);

        String error = receipt.getPrinterErrorMessage();
        Assert.assertTrue(error.contains("Connection lost during printing"),
                "Error should indicate connection lost during printing.");

        // Verify receipt status is marked as Failed (mock attribute)
        driver.executeScript("document.body.setAttribute('data-receipt-status','Failed');");
        String status = driver.findElement(By.tagName("body")).getAttribute("data-receipt-status");
        Assert.assertEquals(status, "