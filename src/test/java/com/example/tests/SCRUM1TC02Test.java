package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.PrinterDiscoveryPage;
import com.example.pages.PrinterConnectionPage;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑02 – Successful printer connection
 */
public class SCRUM1TC02Test extends BaseTest {

    @Test
    public void successfulPrinterConnection() {
        HomePage home = new HomePage(driver);
        home.open();
        PrinterDiscoveryPage discovery = home.goToPrinterDiscovery();

        // Assume printer named "EPSON_TM_P20" exists in the mock list
        PrinterConnectionPage conn = discovery.selectPrinterByName("EPSON_TM_P20");
        conn.confirmConnection();

        String status = conn.getConnectionStatus();
        Assert.assertEquals(status, "Connected", "Printer should be reported as Connected.");
    }
}