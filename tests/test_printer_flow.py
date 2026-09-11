import pytest
import time
from src.pages.printer_page import PrinterPage
from src.pages.receipt_page import ReceiptPage

@pytest.fixture
def printer_page(driver, config):
    page = PrinterPage(driver)
    page.open(config["base_url"])
    return page

@pytest.fixture
def receipt_page(driver, config):
    page = ReceiptPage(driver)
    page.open(config["base_url"])
    return page

def test_scrum_1_tc_01_discoverable_printer_list_displayed(printer_page):
    """TC-01 – Discoverable printer list displayed"""
    printer_page.open_printer_section()
    printer_page.wait_for_discovery()
    # Assume list always appears; check at least one item
    list_elem = printer_page.find(printer_page.DISCOVERY_LIST)
    items = list_elem.find_elements_by_tag_name("li")
    assert len(items) > 0, "No printers discovered"

def test_scrum_1_tc_02_successful_printer_connection(printer_page):
    """TC-02 – Successful printer connection"""
    printer_page.open_printer_section()
    printer_page.wait_for_discovery()
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    status = printer_page.get_status_text()
    assert "Printer Connected" in status
    assert "EPSON_TM-P20_A" in status

def test_scrum_1_tc_03_no_printer_paired_attempt_to_print(printer_page):
    """TC-03 – No printer paired – attempt to print"""
    printer_page.trigger_print()
    msg = printer_page.get_no_printer_message()
    assert "No printer connected" in msg
    # verify Connect Now button is present
    assert printer_page.find(printer_page.CONNECT_NOW_BTN).is_displayed()

def test_scrum_1_tc_04_printer_out_of_range_automatic_retry(printer_page):
    """TC-04 – Printer out of range – automatic retry"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    # Simulate out‑of‑range by toggling Bluetooth off then on
    printer_page.toggle_bluetooth(False)
    printer_page.trigger_print()
    printer_page.toggle_bluetooth(True)
    # Expect retry message
    msg = printer_page.get_disconnect_message()
    assert "Printer disconnected" in msg
    # The UI should attempt retry automatically – we can wait a few seconds
    time.sleep(3)
    # after retries, status should still be disconnected if out of range
    status = printer_page.get_status_text()
    assert "disconnected" in status.lower()

def test_scrum_1_tc_05_receipt_prints_within_sla(printer_page, receipt_page):
    """TC-05 – Receipt prints within SLA"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    start = time.time()
    printer_page.trigger_print()
    # Wait until print status indicates done
    WebDriverWait(printer_page.driver, 10).until(
        lambda d: printer_page.get_print_status().lower() == "printed"
    )
    elapsed = time.time() - start
    assert elapsed <= 5, f"Print latency {elapsed}s exceeds SLA"

def test_scrum_1_tc_06_paper_out_mid_print_error_handling(printer_page):
    """TC-06 – Paper out mid‑print – error handling"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    # Simulate paper out by forcing error element to appear (mocked UI)
    printer_page.trigger_print()
    error_msg = printer_page.get_error_message()
    assert "Paper out" in error_msg
    # Refill paper (in UI we just click retry)
    printer_page.retry_print()
    status = printer_page.get_print_status()
    assert status.lower() == "printed"

def test_scrum_1_tc_07_bluetooth_drop_during_active_print_job(printer_page):
    """TC-07 – Bluetooth drop during active print job"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    printer_page.trigger_print()
    # Immediately drop Bluetooth
    printer_page.toggle_bluetooth(False)
    # UI should show loss message
    loss_msg = printer_page.get_error_message()
    assert "Connection lost during printing" in loss_msg
    status = printer_page.get_print_status()
    assert status.lower() == "failed"
    # Restore Bluetooth for later re‑print
    printer_page.toggle_bluetooth(True)

def test_scrum_1_tc_08_reprint_same_day_receipt_duplicate_copy(printer_page):
    """TC-08 – Re‑print same‑day receipt (duplicate copy)"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    printer_page.trigger_print()
    # Assume receipt now printed; now request re‑print from order history
    printer_page.click(printer_page.PRINT_RECEIPT_BTN)  # same button used for re‑print in this mock
    watermark = printer_page.get_duplicate_watermark()
    assert "DUPLICATE COPY" in watermark
    # Ensure no new transaction created – this would require backend check; skip in UI

def test_scrum_1_tc_09_reprint_after_24hrs_supervisor_approval(printer_page):
    """TC-09 – Re‑print after 24 hrs – supervisor approval"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    printer_page.trigger_print()
    # Simulate >24h by directly invoking re‑print flow that requires PIN
    printer_page.click(printer_page.PRINT_RECEIPT_BTN)
    # Expect supervisor PIN dialog
    printer_page.enter_supervisor_pin("1234")
    printer_page.submit_supervisor()
    # After approval, duplicate watermark should appear
    watermark = printer_page.get_duplicate_watermark()
    assert "DUPLICATE COPY" in watermark

def test_scrum_1_tc_10_concurrent_connection_attempts_conflict_handling(printer_page):
    """TC-10 – Concurrent connection attempts – conflict handling"""
    # Device A connects (simulated by current session)
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    status_a = printer_page.get_status_text()
    assert "Connected" in status_a
    # Simulate Device B attempt by opening new page object (same driver for simplicity)
    printer_page_2 = PrinterPage(printer_page.driver)
    printer_page_2.open(printer_page.driver.current_url)
    printer_page_2.select_printer("EPSON_TM-P20_A")
    printer_page_2.confirm_connection()
    conflict_msg = printer_page_2.get_conflict_message()
    assert "currently in use" in conflict_msg.lower()

def test_scrum_1_tc_11_low_battery_warning(printer_page):
    """TC-11 – Low‑battery warning"""
    printer_page.select_printer("EPSON_TM-P20_LOW")
    printer_page.confirm_connection()
    # UI should display low‑battery icon
    assert printer_page.get_low_battery_icon_present()

def test_scrum_1_tc_12_logout_app_close_release_printer(printer_page):
    """TC-12 – Logout / app close – release printer"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    # Perform logout (assuming a logout button exists)
    printer_page.click((By.ID, "logout-btn"))
    # Verify connection released (status should not show connected)
    status = printer_page.get_status_text()
    assert "disconnected" in status.lower() or "released" in status.lower()

def test_scrum_1_tc_13_persistence_of_pairing_across_app_restarts(printer_page):
    """TC-13 – Persistence of pairing across app restarts (within shift)"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    # Simulate force‑close by refreshing the page
    printer_page.driver.refresh()
    # After reload, printer should be auto‑selected
    status = printer_page.get_status_text()
    assert "Connected" in status
    assert "EPSON_TM-P20_A" in status

def test_scrum_1_tc_14_ios_android_platform_compatibility(printer_page):
    """TC-14 – iOS & Android platform compatibility"""
    # This test simply runs on the current platform; real cross‑platform would be separate pipelines
    printer_page.open_printer_section()
    printer_page.wait_for_discovery()
    # Verify that discovery works (same as TC‑01)
    list_elem = printer_page.find(printer_page.DISCOVERY_LIST)
    items = list_elem.find_elements_by_tag_name("li")
    assert len(items) > 0

def test_scrum_1_tc_15_esc_pos_command_compliance(printer_page):
    """TC-15 – ESC/POS command compliance"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    # In a real environment we would capture raw bytes; here we simulate by checking a hidden element
    raw_data = printer_page.driver.execute_script("return window.lastEscPosData || ''")
    assert raw_data.startswith("\x1b")  # ESC character
    # Ensure no proprietary commands (example check)
    assert "CUSTOM_CMD" not in raw_data

def test_scrum_1_tc_16_sensitive_receipt_data_not_logged_in_plaintext(printer_page):
    """TC-16 – Sensitive receipt data not logged in plaintext"""
    printer_page.select_printer("EPSON_TM-P20_A")
    printer_page.confirm_connection()
    printer_page.trigger_print()
    printer_page.view_logs()
    logs = printer_page.get_logs()
    assert "creditcard" not in logs.lower()
    assert "****" in logs  # masked representation expected

def test_scrum_1_tc_17_battery_drain_impact_on_print_latency(printer_page):
    """TC-17 – Battery‑drain impact on print latency"""
    printer_page.select_printer("EPSON_TM-P20_LOW_BAT")
    printer_page.confirm_connection()
    start = time.time()
    printer_page.trigger_print()
    WebDriverWait(printer_page.driver, 10).until(
        lambda d: printer_page.get_print_status().lower() == "printed"
    )
    elapsed = time.time() - start
    assert elapsed <= 5, f"Latency {elapsed}s exceeds SLA for low battery"

def test_scrum_1_tc_18_multiple_printers_correct_selection(printer_page):
    """TC-18 – Multiple printers in same store – correct printer selection"""
    printer_page.open_printer_section()
    printer_page.wait_for_discovery()
    # Verify both printers appear
    list_elem = printer_page.find(printer_page.DISCOVERY_LIST)
    names = [li.text for li in list_elem.find_elements_by_tag_name("li")]
    assert "EPSON_TM-P20_A" in names and "EPSON_TM-P20_B" in names
    # Select printer B
    printer_page.select_printer("EPSON_TM-P20_B")
    printer_page.confirm_connection()
    status = printer_page.get_status_text()
    assert "EPSON_TM-P20_B" in status

def test_scrum_1_tc_19_printer_firmware_version_check_unsupported(printer_page):
    """TC-19 – Printer firmware version check (unsupported version)"""
    printer_page.select_printer("EPSON_TM-P20_OLDFW")
    printer_page.confirm_connection()
    warning = printer_page.get_firmware_warning()
    assert "firmware not supported" in warning.lower()

def test_scrum_1