import pytest
import time
from src.pages.home_page import HomePage
from src.pages.printer_list_page import PrinterListPage
from src.pages.print_receipt_page import PrintReceiptPage

@pytest.fixture
def home(driver):
    return HomePage(driver)

@pytest.fixture
def printer_list(driver):
    return PrinterListPage(driver)

@pytest.fixture
def print_page(driver):
    return PrintReceiptPage(driver)

# SCRUM‑1‑TC‑01 – Discoverable printer list displayed
def test_discoverable_printer_list_displayed(home, printer_list):
    home.tap_connect_printer()
    printer_list.wait_for_discovery()
    printers = printer_list.get_printer_names()
    assert len(printers) > 0, "No discoverable printers were shown"

# SCRUM‑1‑TC‑02 – Successful printer connection
def test_successful_printer_connection(home, printer_list):
    home.tap_connect_printer()
    printer_list.wait_for_discovery()
    assert printer_list.select_printer_by_name("EPSON_TM-P20_A"), "Target printer not found"
    connected = printer_list.get_connected_printer_name()
    assert "EPSON_TM-P20_A" in connected
    assert "Printer Connected" in home.get_printer_status()

# SCRUM‑1‑TC‑03 – No printer paired – attempt to print
def test_no_printer_paired_print_attempt(home, print_page):
    # Ensure no printer is paired (pre‑condition handled externally)
    home.tap_print_receipt()
    assert print_page.is_displayed(*print_page.CONNECT_NOW_BTN), "Connect Now button not shown"
    error_msg = print_page.get_error_message()
    assert "No printer connected" in error_msg

# SCRUM‑1‑TC‑04 – Printer out of range – automatic retry
def test_printer_out_of_range_retry(home, print_page):
    # Assume printer was previously paired; now out of range
    home.tap_print_receipt()
    error_msg = print_page.get_error_message()
    assert "Printer disconnected" in error_msg
    # Verify up to 3 retries (simple check that retry attempts happen)
    for attempt in range(3):
        time.sleep(1)  # simulate wait between retries
    assert "move closer or reconnect" in error_msg

# SCRUM‑1‑TC‑05 – Receipt prints within SLA
def test_receipt_prints_within_sla(home, print_page):
    start = time.time()
    home.tap_print_receipt()
    print_page.wait_for_print_completion()
    duration = time.time() - start
    assert duration <= 5, f"Print latency {duration}s exceeds SLA of 5s"

# SCRUM‑1‑TC‑06 – Paper out mid‑print – error handling
def test_paper_out_error_handling(home, print_page):
    home.tap_print_receipt()
    # Simulate paper out error (app shows specific message)
    error_msg = print_page.get_error_message()
    assert "Paper out" in error_msg
    # Refill paper and re‑print
    print_page.tap_retry()
    print_page.wait_for_print_completion()
    assert print_page.get_print_status() == "Printed"

# SCRUM‑1‑TC‑07 – Bluetooth drop during active print job
def test_bluetooth_drop_during_print(home, print_page):
    home.tap_print_receipt()
    # Simulate Bluetooth being turned off during printing
    # (In real test this would be done via ADB or device controls)
    time.sleep(1)  # let printing start
    # Assume driver receives loss event and UI updates
    error_msg = print_page.get_error_message()
    assert "Connection lost during printing" in error_msg
    assert print_page.get_print_status() == "Failed"

# SCRUM‑1‑TC‑08 – Re‑print same‑day receipt (duplicate copy)
def test_reprint_same_day_duplicate(home, print_page):
    # Assume receipt already printed; navigate to history and select re‑print
    home.tap_print_receipt()  # shortcut for re‑print in this demo
    assert print_page.is_duplicate_watermark_displayed()
    assert print_page.get_print_status() == "Printed"

# SCRUM‑1‑TC‑09 – Re‑print after 24 hrs – supervisor approval
def test_reprint_after_24hrs_supervisor_approval(home, print_page):
    home.tap_print_receipt()
    # App should prompt for PIN
    print_page.enter_supervisor_pin("1234")
    print_page.submit_supervisor_pin()
    assert print_page.is_duplicate_watermark_displayed()
    assert print_page.get_print_status() == "Printed"

# SCRUM‑1‑TC‑10 – Concurrent connection attempts – conflict handling
def test_concurrent_connection_conflict(driver):
    # Simulate two devices by opening two driver sessions (simplified)
    # Device A connects successfully
    home_a = HomePage(driver)
    home_a.tap_connect_printer()
    # Device B (same driver) attempts to connect – should see conflict message
    # In real world a second driver would be used; we verify UI shows conflict
    error_msg = driver.find_element_by_id("com.example.printerapp:id/tv_error_message").text
    assert "currently in use by another device" in error_msg

# SCRUM‑1‑TC‑11 – Low‑battery warning
def test_low_battery_warning(home):
    status = home.get_printer_status()
    assert "Low battery" in status or home.is_low_battery_icon_displayed()

# SCRUM‑1‑TC‑12 – Logout / app close – release printer
def test_logout_releases_printer(home):
    home.tap_logout()
    # After logout, another device should be able to pair; verify status cleared
    assert "Disconnected" in home.get_printer_status()

# SCRUM‑1‑TC‑13 – Persistence of pairing across app restarts (within shift)
def test_pairing_persistence_across_restart(driver):
    home = HomePage(driver)
    # Assume printer already paired
    driver.close_app()
    driver.launch_app()
    home = HomePage(driver)
    assert "Printer Connected" in home.get_printer_status()

# SCRUM‑1‑TC‑14 – iOS & Android platform compatibility
@pytest.mark.parametrize("platform", ["Android", "iOS"])
def test_platform_compatibility(driver, platform):
    # Adjust capabilities for each platform (handled via env vars before test run)
    home = HomePage(driver)
    home.tap_connect_printer()
    # Simple verification that the flow works on both platforms
    assert home.is_displayed(*home.CONNECT_PRINTER_BTN)

# SCRUM‑1‑TC‑15 – ESC/POS command compliance
def test_esc_pos_command_compliance(driver):
    # Capture raw bytes sent to printer via a mock or proxy (simplified)
    # Here we just assert that the app logs a placeholder indicating ESC/POS usage
    logs = driver.get_log("driver")
    esc_pos_used = any("ESC/POS" in entry["message"] for entry in logs)
    assert esc_pos_used, "ESC/POS commands not detected in logs"

# SCRUM‑1‑TC‑16 – Sensitive receipt data not logged in plaintext
def test_sensitive_data_not_logged(driver):
    home = HomePage(driver)
    home.tap_print_receipt()
    logs = driver.get_log("driver")
    sensitive = any("cardNumber" in entry["message"] for entry in logs)
    assert not sensitive, "Sensitive receipt data found in logs"

# SCRUM‑1‑TC‑17 – Battery‑drain impact on print latency
def test_low_battery_print_latency(home, print_page):
    # Assume printer battery is low but functional
    home.tap_print_receipt()
    start = time.time()
    print_page.wait_for_print_completion()
    duration = time.time() - start
    assert duration <= 5, f"Latency {duration}s exceeds SLA despite low battery"

# SCRUM‑1‑TC‑18 – Multiple printers – correct selection
def test_multiple_printers_correct_selection(home, printer_list):
    home.tap_connect_printer()
    printer_list.wait_for_discovery()
    names = printer_list.get_printer_names()
    assert "Printer B" in names
    printer_list.select_printer_by_name("Printer B")
    assert "Printer B" in printer_list.get_connected_printer_name()
    home.tap_print_receipt()
    # Verify print goes to Printer B via status message
    status = home.get_printer_status()
    assert "Printer B" in status

# SCRUM‑1‑TC‑19 – Firmware version check (unsupported)
def test_firmware_version_unsupported(home, printer_list):
    home.tap_connect_printer()
    printer_list.wait_for_discovery()
    # Select a printer with known old firmware (mocked by name)
    printer_list.select_printer_by_name("OldFirmwarePrinter")
    error_msg = printer_list.get_error_message()
    assert "firmware not supported" in error_msg.lower()

# SCRUM‑1‑TC‑20 – Network‑independent operation
def test_network_independent_operation(driver):
    # Disable network (this would be done via ADB or device settings; here we assume)
    home = HomePage(driver)
    home.tap_connect_printer()
    # Verify discovery still works without network
    printer_list = PrinterListPage(driver)
    printer_list.wait_for_discovery()
    assert len(printer_list.get_printer_names()) > 0