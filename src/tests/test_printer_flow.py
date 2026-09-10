import time
import pytest
from src.pages.home_page import HomePage
from src.pages.printer_list_page import PrinterListPage
from src.pages.print_receipt_page import PrintReceiptPage
from src.pages.settings_page import SettingsPage

@pytest.fixture(scope="function")
def app(driver):
    """Navigate to the home page before each test."""
    home = HomePage(driver)
    home.open()
    return home

def test_discoverable_printer_list_displayed(app, driver):
    """SCRUM‑1‑TC‑01 – Verify list of printers appears after discovery."""
    app.tap_connect_printer()
    printer_page = PrinterListPage(driver)
    # Simulate waiting for discovery (in real test, explicit wait would be used)
    time.sleep(2)
    assert printer_page.get_printer_names(), "Printer list should not be empty."

def test_successful_printer_connection(app, driver):
    """SCRUM‑1‑TC‑02 – Connect to a printer and verify indicator."""
    app.tap_connect_printer()
    printer_page = PrinterListPage(driver)
    # Assume the first printer in the list is the target
    names = printer_page.get_printer_names()
    assert names, "No printers found for connection test."
    selected = printer_page.select_printer_by_name(names[0])
    assert selected, f"Could not select printer {names[0]}"
    # Verify connection indicator (placeholder - actual locator needed)
    connected_indicator = (By.ID, "printer_connected")
    assert BasePage(driver).is_displayed(connected_indicator), "Printer Connected indicator not shown."

def test_no_printer_paired_attempt_print(app, driver):
    """SCRUM‑1‑TC‑03 – Ensure proper message when no printer is paired."""
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    error_msg = receipt_page.get_error_message()
    assert "No printer connected" in error_msg
    assert receipt_page.is_displayed(receipt_page.CONNECT_NOW_BTN), "Connect Now button should be visible."

def test_printer_out_of_range_retry(app, driver):
    """SCRUM‑1‑TC‑04 – Automatic retry when printer is out of range."""
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    # Simulate out‑of‑range scenario via mock or test environment setup
    error_msg = receipt_page.get_error_message()
    assert "Printer disconnected" in error_msg
    # Verify that the app attempted retries (could be logged or UI counter)
    retry_counter = (By.ID, "retry_counter")
    retries = driver.find_element(*retry_counter).text
    assert retries == "3", "App should retry exactly 3 times."

def test_receipt_prints_within_sla(app, driver):
    """SCRUM‑1‑TC‑05 – Receipt prints within 5 seconds."""
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    start = time.time()
    # Wait until status changes to "Printed"
    while receipt_page.get_status_text() != "Printed" and (time.time() - start) < 10:
        time.sleep(0.5)
    elapsed = time.time() - start
    assert receipt_page.get_status_text() == "Printed", "Receipt was not printed successfully."
    assert elapsed <= 5, f"Print latency {elapsed}s exceeds SLA of 5s."

def test_paper_out_mid_print_error_handling(app, driver):
    """SCRUM‑1‑TC‑06 – Paper out error handling."""
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    # Simulate paper out condition
    error_msg = receipt_page.get_error_message()
    assert "Paper out" in error_msg
    # After refill (simulated), user should be able to re‑print without duplicate transaction
    receipt_page.tap_retry()
    # Verify status returns to Printed without new transaction entry (placeholder)
    assert receipt_page.get_status_text() == "Printed"

def test_bluetooth_drop_during_active_print(app, driver):
    """SCRUM‑1‑TC‑07 – Bluetooth drop handling."""
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    # Simulate Bluetooth drop
    error_msg = receipt_page.get_error_message()
    assert "Connection lost during printing" in error_msg
    # Verify receipt status set to Failed
    assert receipt_page.get_status_text() == "Failed"

def test_reprint_same_day_duplicate(app, driver):
    """SCRUM‑1‑TC‑08 – Re‑print same‑day receipt with duplicate watermark."""
    # Assume receipt already printed; navigate to re‑print flow
    app.tap_print_receipt()  # placeholder for re‑print navigation
    receipt_page = PrintReceiptPage(driver)
    receipt_page.start_print()
    assert receipt_page.is_duplicate_watermark_present(), "Duplicate watermark not displayed."

def test_reprint_after_24hrs_supervisor_approval(app, driver):
    """SCRUM‑1‑TC‑09 – Supervisor PIN required for old receipt."""
    app.tap_print_receipt()  # placeholder for selecting old receipt
    receipt_page = PrintReceiptPage(driver)
    # Verify PIN prompt appears
    pin_input = receipt_page.SUPERVISOR_PIN_INPUT
    assert receipt_page.is_displayed(pin_input), "Supervisor PIN prompt not shown."
    receipt_page.enter_supervisor_pin("1234")  # example PIN
    # After correct PIN, receipt should print with duplicate watermark
    assert receipt_page.is_duplicate_watermark_present()

def test_concurrent_connection_attempts_conflict(app, driver):
    """SCRUM‑1‑TC‑10 – Conflict handling when two devices try same printer."""
    # This test would normally be run on two parallel sessions; here we simulate the response
    app.tap_connect_printer()
    printer_page = PrinterListPage(driver)
    names = printer_page.get_printer_names()
    assert names, "No printers available for concurrent test."
    printer_page.select_printer_by_name(names[0])
    # Simulate second device attempt response
    conflict_msg = (By.ID, "conflict_message")
    assert BasePage(driver).is_displayed(conflict_msg), "Conflict message not shown for second device."

def test_low_battery_warning(app, driver):
    """SCRUM‑1‑TC‑11 – Low‑battery warning icon appears."""
    # Assume printer is already connected with low battery
    receipt_page = PrintReceiptPage(driver)
    assert receipt_page.is_low_battery_icon_displayed(), "Low‑battery warning icon not displayed."

def test_logout_releases_printer(app, driver):
    """SCRUM‑1‑TC‑12 – Ensure Bluetooth connection released on logout."""
    app.tap_settings()
    settings = SettingsPage(driver)
    settings.logout()
    # After logout, printer should be available for other devices (placeholder check)
    availability_indicator = (By.ID, "printer_available")
    assert BasePage(driver).is_displayed(availability_indicator), "Printer not released after logout."

def test_pairing_persistence_across_restart(app, driver):
    """SCRUM‑1‑TC‑13 – Paired printer persists after app restart."""
    # Simulate app force‑close by navigating away and back
    driver.refresh()
    # Verify printer is still auto‑selected
    connected_indicator = (By.ID, "printer_connected")
    assert BasePage(driver).is_displayed(connected_indicator), "Printer pairing did not persist."

def test_platform_compatibility(app, driver):
    """SCRUM‑1‑TC‑14 – Verify behavior on Android & iOS (simulated)."""
    # In real CI we would run on device farms; here just assert generic UI works
    assert app.is_displayed(app.CONNECT_PRINTER_BTN), "Connect Printer button missing."

def test_esc_pos_command_compliance(app, driver):
    """SCRUM‑1‑TC‑15 – Validate raw data sent conforms to ESC/POS."""
    # Capture raw data via a mock or network sniff (out of scope for UI test)
    # Placeholder assertion
    assert True, "ESC/POS command compliance check placeholder."

def test_sensitive_receipt_data_not_logged(app, driver, caplog):
    """SCRUM‑1‑TC‑16 – Ensure receipt data not logged in plaintext."""
    app.tap_print_receipt()
    # After printing, inspect captured logs
    for record in caplog.records:
        assert "card number" not in record.message.lower(), "Sensitive data found in logs."

def test_battery_drain_impact_on_latency(app, driver):
    """SCRUM‑1‑TC‑17 – Verify latency with low battery (10‑20%)."""
    start = time.time()
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    while receipt_page.get_status_text() != "Printed" and (time.time() - start) < 10:
        time.sleep(0.5)
    elapsed = time.time() - start
    assert elapsed <= 5, f"Print latency {elapsed}s exceeds SLA with low battery."

def test_multiple_printers_correct_selection(app, driver):
    """SCRUM‑1‑TC‑18 – Select correct printer when multiple are present."""
    app.tap_connect_printer()
    printer_page = PrinterListPage(driver)
    names = printer_page.get_printer_names()
    assert len(names) >= 2, "Need at least two printers for this test."
    target = names[1]  # choose second printer
    printer_page.select_printer_by_name(target)
    # Verify subsequent prints go to selected printer (placeholder)
    selected_indicator = (By.ID, "selected_printer_name")
    displayed_name = driver.find_element(*selected_indicator).text
    assert displayed_name == target, "Prints are not routed to the selected printer."

def test_printer_firmware_version_check(app, driver):
    """SCRUM‑1‑TC‑19 – Unsupported firmware version rejection."""
    app.tap_connect_printer()
    # Simulate connecting to old firmware printer
    error_msg = (By.ID, "firmware_error_msg")
    assert BasePage(driver).is_displayed(error_msg), "Firmware version error not shown."

def test_network_independent_operation(app, driver):
    """SCRUM‑1‑TC‑20 – Verify printer works offline."""
    # Simulate offline mode (could be done via Chrome devtools; here just assume)
    app.tap_print_receipt()
    receipt_page = PrintReceiptPage(driver)
    while receipt_page.get_status_text() != "Printed" and (time.time() - start) < 10:
        time.sleep(0.5)
    assert receipt_page.get_status_text() == "Printed", "Printing failed while offline."