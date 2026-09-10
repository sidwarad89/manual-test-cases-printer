package com.example.tests;

import com.example.pages.HomePage;
import com.example.pages.PrinterDiscoveryPage;
import com.example.pages.PrinterConnectionPage;
import org.testng.Assert;
import org.testng.annotations.Test;

/**
 * TC SCRUM‑1‑TC‑01 – Discoverable printer list displayed
 */
public class SCRUM1TC01Test extends BaseTest {

    @Test
    public void discoverablePrinterListDisplayed() {
        HomePage home = new HomePage(driver);
        home.open();
        PrinterDiscoveryPage discovery = home.goToPrinterDiscovery();

        discovery.refreshList();

        // Verify at least one printer appears (the list may be mocked in test environment)
        Assert.assertTrue(discovery.getAvailablePrinters().size() > 0,
                "Printer list should contain at least one discoverable or paired printer.");
    }
}