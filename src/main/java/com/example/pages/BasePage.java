package com.example.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

/**
 * Base class for all page objects. Holds the common driver and wait instances.
 */
public class BasePage {
    protected WebDriver driver;
    protected WebDriverWait wait;

    public BasePage(WebDriver driver) {
        this.driver = driver;
        // Default explicit wait of 10 seconds
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    /**
     * Simple navigation helper.
     */
    public void navigateTo(String url) {
        driver.get(url);
    }
}