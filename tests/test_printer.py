import pytest
import time
from pages.printer_page import PrinterPage

# Helper constants (adjust to your environment)
TEST_PRINTER_A = "EPSON_TM_P20_A"
TEST_PRINTER_B = "EPSON_TM_P20_B"
SUPERVISOR_PIN = "1234"

@pytest.mark.timeout(120)
def test_discoverable_printer_list_displayed(driver):
    """SCRUM‑1‑TC‑01 – Discoverable printer list displayed"""
    page = PrinterPage(driver)
    page.open_printer_discovery()
    printers = page.get_discovered_printers()
    assert len(printers) > 0, "No printers were discovered"
    # Ensure at least one known printer is in the list (optional)
    assert any(p.startswith("EPSON") for p in printers)

@pytest.mark.timeout(120)
def test_successful_printer_connection(driver):
    """SCRUM‑1‑TC‑02 – Successful printer connection"""
    page = PrinterPage(driver)
    page.open_printer_discovery()
    printers = page.get_discovered_printers()
    assert TEST_PRINTER_A in printers, f"{TEST_PRINTER_A} not found"
    page.select_printer(TEST_PRINTER_A)
    # Verify connection indicator
    assert page.is_printer_connected()
    status = page.get_connection_status_text()
    assert TEST_PRINTER_A in status

@pytest.mark.timeout(120)
def test_no_printer_paired_attempt_to_print(driver):
    """SCRUM‑1‑TC‑03 – No printer paired – attempt to print"""
    page = PrinterPage(driver)
    # Ensure no printer is connected – this would be part of pre‑condition setup
    page.trigger_print()
    msg = page.get_no_printer_message()
    assert "No printer connected" in msg
    # Verify Connect Now button is present
    assert page.is_displayed(page.CONNECT_NOW_BUTTON)

@pytest.mark.timeout(180)
def test_printer_out_of_range_automatic_retry(driver):
    """SCRUM‑1‑TC‑04 – Printer out of range – automatic retry"""
    page = PrinterPage(driver)
    # Assume printer already paired; we just attempt print
    page.trigger_print()
    error = page.get_error_message()
    assert "Printer disconnected" in error
    # Verify retry attempts (simulated by checking retry button)
    for attempt in range(3):
        page.retry_connection()
        # In real test we would wait and re‑check error; simplified:
        time.sleep(2)
    final_error = page.get_error_message()
    assert "Printer disconnected" in final_error

@pytest.mark.timeout(30)
def test_receipt_prints_within_sla(driver):
    """SCRUM‑1‑TC‑05 – Receipt prints within SLA"""
    page = PrinterPage(driver)
    start = time.time()
    page.complete_sale_and_print()
    # Wait for some UI element that indicates print success
    page.wait_for_visibility(page.CONNECTED_INDICATOR, timeout=10)
    elapsed = time.time() - start
    assert elapsed <= 5, f"Print latency {elapsed}s exceeds SLA"

@pytest.mark.timeout(120)
def test_paper_out_mid_print_error_handling(driver):
    """SCRUM‑1‑TC‑06 – Paper out mid‑print – error handling"""
    page = PrinterPage(driver)
    page.trigger_print()
    error = page.get_error_message()
    assert "Paper out" in error
    # Simulate user refilling paper and re‑printing
    # In a real device this would be a physical action; we just retry
    page.retry_connection()
    page.trigger_print()
    # Confirm no duplicate transaction (placeholder check)
    assert not page.is_displayed(page.DUPLICATE_WATERMARK)

@pytest.mark.timeout(120)
def test_bluetooth_drop_during_active_print_job(driver):
    """SCRUM‑1‑TC‑07 – Bluetooth drop during active print job"""
    page = PrinterPage(driver)
    page.trigger_print()
    # Simulate Bluetooth disable – in real test use driver.toggle_airplane_mode or similar
    # Here we just wait for error
    error = page.get_error_message()
    assert "Connection lost during printing" in error
    # Verify receipt status set to Failed (placeholder)
    status = page.get_connection_status_text()
    assert "Failed" in status

@pytest.mark.timeout(120)
def test_reprint_same_day_receipt_duplicate_copy(driver):
    """SCRUM‑1‑TC‑08 – Re‑print same‑day receipt (duplicate copy)"""
    page = PrinterPage(driver)
    # Assume receipt already printed; navigate to history and select reprint
    # Placeholder: directly trigger reprint
    page.trigger_print()
    assert page.is_duplicate_watermark_displayed()

@pytest.mark.timeout(120)
def test_reprint_after_24hrs_supervisor_approval(driver):
    """SCRUM‑1‑TC‑09 – Re‑print after 24 hrs – supervisor approval"""
    page = PrinterPage(driver)
    page.trigger_print()
    # Expect supervisor PIN prompt
    page.enter_supervisor_pin(SUPERVISOR_PIN)
    # After approval, duplicate watermark should appear
    assert page.is_duplicate_watermark_displayed()

@pytest.mark.timeout(120)
def test_concurrent_connection_attempts_conflict_handling(driver):
    """SCRUM‑1‑TC‑10 – Concurrent connection attempts – conflict handling"""
    # This test would require two devices; we simulate the conflict response
    page = PrinterPage(driver)
    page.open_printer_discovery()
    # Simulate that another device already connected
    # Attempt to connect and verify error message
    try:
        page.select_printer(TEST_PRINTER_A)
    except Exception:
        pytest.fail("Failed to select printer")
    error = page.get_error_message()
    assert "currently in use" in error

@pytest.mark.timeout(120)
def test_low_battery_warning_displayed(driver):
    """SCRUM‑1‑TC‑11 – Low‑battery warning"""
    page = PrinterPage(driver)
    # Assume printer connected with low battery
    assert page.is_low_battery_icon_displayed()

@pytest.mark.timeout(120)
def test_logout_app_close_releases_printer(driver):
    """SCRUM‑1‑TC‑12 – Logout / app close – release printer"""
    page = PrinterPage(driver)
    # Simulate logout
    # Placeholder: tap logout button (locator not defined)
    logout_button = (MobileBy.ACCESSIBILITY_ID, "Logout")
    page.click(logout_button)
    # Verify printer is no longer connected
    assert not page.is_printer_connected()

@pytest.mark.timeout(120)
def test_persistence_of_pairing_across_app_restart(driver):
    """SCRUM‑1‑TC‑13 – Persistence of pairing across app restarts (within shift)"""
    page = PrinterPage(driver)
    # Assume printer was paired earlier
    # Force close app
    driver.terminate_app(driver.capabilities['appPackage'])
    driver.activate_app(driver.capabilities['appPackage'])
    # Verify auto‑selected printer
    assert page.is_printer_connected()

@pytest.mark.timeout(120)
def test_ios_android_platform_compatibility(driver):
    """SCRUM‑1‑TC‑14 – iOS & Android platform compatibility"""
    # The fixture already runs on both platforms; just assert a simple UI element
    page = PrinterPage(driver)
    page.open_printer_discovery()
    assert page.is_displayed(page.PRINTER_LIST)

@pytest.mark.timeout(120)
def test_esc_pos_command_compliance(driver):
    """SCRUM‑1‑TC‑15 – ESC/POS command compliance"""
    # Capturing raw data sent to printer would need device-side logs; we simulate check
    page = PrinterPage(driver)
    page.trigger_print()
    # Placeholder: assume we can retrieve raw command log
    raw_data = driver.execute_script("mobile: shell", {
        "command": "cat",
        "args": ["/data/local/tmp/last_printer_output.bin"],
        "includeStderr": True,
        "timeout": 5000
    })
    assert b'\x1b' in raw_data  # ESC character typical of ESC/POS
    # Further validation would parse commands – omitted for brevity

@pytest.mark.timeout(120)
def test_sensitive_receipt_data_not_logged_plaintext(driver, caplog):
    """SCRUM‑1‑TC‑16 – Sensitive receipt data not logged in plaintext"""
    page = PrinterPage(driver)
    with caplog.at_level("INFO"):
        page.trigger_print()
    logs = "\n".join(record.message for record in caplog.records)
    assert "credit card" not in logs.lower()
    assert "****" in logs  # masked representation expected

@pytest.mark.timeout(120)
def test_battery_drain_impact_on_print_latency(driver):
    """SCRUM‑1‑TC‑17 – Battery‑drain impact on print latency"""
    page = PrinterPage(driver)
    start = time.time()
    page.trigger_print()
    page.wait_for_visibility(page.CONNECTED_INDICATOR, timeout=10)
    elapsed = time.time() - start
    assert elapsed <= 5, f"Latency {elapsed}s exceeds SLA for low battery"

@pytest.mark.timeout(120)
def test_multiple_printers_correct_selection(driver):
    """SCRUM‑1‑TC‑18 – Multiple printers in same store – correct printer selection"""
    page = PrinterPage(driver)
    page.open_printer_discovery()
    printers = page.get_discovered_printers()
    assert TEST_PRINTER_A in printers and TEST_PRINTER_B in printers
    page.select_printer(TEST_PRINTER_B)
    assert page.get_connection_status_text() == TEST_PRINTER_B

@pytest.mark.timeout(120)
def test_printer_firmware_version_check_unsupported(driver):
    """SCRUM‑1‑TC‑19 – Printer firmware version check (unsupported version)"""
    page = PrinterPage(driver)
    page.open_printer_discovery()
    # Assume an old firmware printer is listed with a specific name
    old_firmware_printer = "EPSON_OLD_FW"
    printers = page.get_discovered_printers()
    assert old_firmware_printer in printers
    page.select_printer(old_firmware_printer)
    error = page.get_error_message()
    assert "firmware not supported" in error.lower()

@pytest.mark.timeout(120)
def test_network_independent_operation(driver):
    """SCRUM‑1‑TC‑20 – Network‑independent operation"""
    # Simulate offline mode: disable Wi‑Fi and cellular
    driver.set_network_connection(0)  # 0 = Airplane mode (no network)
    page = PrinterPage(driver)
    page.trigger_print()
    # Expect print to succeed without network calls
    assert page.is_printer_connected()
    # Reset network for other tests
    driver.set_network_connection(6)  # 6 = All network on (Wi‑Fi + data)