package com.example.pages;

import org.openqa.selenium.WebDriver;

/**
 * Settings / logout page.
 */
public class SettingsPage extends BasePage {

    private By confirmLogoutBtn = By.id("confirm-logout");

    public SettingsPage(WebDriver driver) {
        super(driver);
    }

    public void logout() {
        driver.findElement(confirmLogoutBtn).click();
    }
}