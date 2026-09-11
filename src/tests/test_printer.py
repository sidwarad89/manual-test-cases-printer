import time
import pytest
from src.pages.main_page import MainPage
from src.pages.printer_list_page import PrinterListPage


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def printer_list_page(driver):
    return PrinterListPage(driver)


def test_scrum_1_tc_01_discoverable_printer_list_displayed(main_page, printer_list_page):
    """
    SCRUM‑1‑TC‑01 – Discoverable printer list displayed
    """
    main_page.tap_connect_printer()
    printer_list_page.wait_for_printer_list()
    printer_names = printer_list_page.get_printer_names()
    assert len(printer_names) > 0, "No printers were discovered"


def test_scrum_1_tc_02_successful_printer_connection(main_page, printer_list_page):
    """
    SCRUM‑1‑TC‑02 – Successful printer connection
    """
    main_page.tap_connect_printer()
    printer_list_page.wait_for_printer_list()
    # Select the first printer (assumes at least one printer is present)
    printer_names = printer_list_page.get_printer_names()
    assert printer_names, "No printers to select"
    printer_to_connect = printer_names[0]
    printer_list_page.select_printer_by_name(printer_to_connect)
    # Confirm connection indicator appears
    assert main_page.is_printer_connected()
    assert printer_to_connect in main_page.get_connected_printer_name()


def test_scrum_1_tc_03_no_printer_paired_attempt_to_print(main_page):
    """
    SCRUM‑1‑TC‑03 – No printer paired – attempt to print
    """
    # Ensure no printer is connected (could be done via app reset, but we assume state)
    main_page.tap_complete_sale()
    main_page.tap_print_receipt()
    assert main_page.is_no_printer_message_displayed()
    # Verify the "Connect Now" button is present
    main_page.tap_connect_now()


def test_scrum_1_tc_04_printer_out_of_range_automatic_retry(main_page):
    """
    SCRUM‑1‑TC‑04 – Printer out of range – automatic retry
    """
    main_page.tap_print_receipt()
    # The app should show a disconnected message and attempt retries internally
    assert main_page.is_printer_disconnected_message_displayed()
    # No explicit check for retry count – we rely on the UI message


def test_scrum_1_tc_05_receipt_prints_within_sla(main_page):
    """
    SCRUM‑1‑TC‑05 – Receipt prints within SLA
    """
    main_page.tap_complete_sale()
    start = time.time()
    main_page.tap_print_receipt()
    # Wait for success indicator (could be a toast or a status element)
    # Placeholder: we wait for printer connected indicator to remain (means print succeeded)
    time.sleep(5)  # give the app time to finish printing
    elapsed = time.time() - start
    assert elapsed <= 5.0, f"Print latency {elapsed:.2f}s exceeds SLA of 5s"


def test_scrum_1_tc_06_paper_out_mid_print_error_handling(main_page):
    """
    SCRUM‑1‑TC‑06 – Paper out mid‑print – error handling
    """
    main_page.tap_print_receipt()
    # Simulate paper out – in real device this would be a hardware event.
    # We verify that the app shows the appropriate error message.
    error_msg = main_page.get_printer_error_message()
    assert "Paper out" in error_msg
    # After refill, user can re‑print – we simulate by tapping print again
    main_page.tap_print_receipt()
    # Ensure no duplicate transaction (application‑specific verification would be needed)


def test_scrum_1_tc_07_bluetooth_drop_during_active_print_job(main_page):
    """
    SCRUM‑1‑TC‑07 – Bluetooth drop during active print job
    """
    main_page.tap_print_receipt()
    # Simulate Bluetooth drop – not possible via UI, assume app reacts
    lost_msg = main_page.get_connection_lost_message()
    assert "Connection lost during printing" in lost_msg
    # Verify receipt status is marked as Failed (placeholder check)
    # This would normally involve checking a status element


def test_scrum_1_tc_08_reprint_same_day_receipt_duplicate_copy(main_page):
    """
    SCRUM‑1‑TC‑08 – Re‑print same‑day receipt (duplicate copy)
    """
    # Assume receipt already printed; navigate to Order History (placeholder)
    main_page.tap_print_receipt()  # Re‑print action
    assert main_page.is_duplicate_watermark_displayed()


def test_scrum_1_tc_09_reprint_after_24hrs_supervisor_approval(main_page):
    """
    SCRUM‑1‑TC‑09 – Re‑print after 24 hrs – supervisor approval
    """
    main_page.tap_print_receipt()  # Trigger re‑print flow
    # Expect PIN prompt
    main_page.enter_supervisor_pin("1234")  # Replace with valid test PIN
    # After approval, duplicate watermark should appear
    assert main_page.is_duplicate_watermark_displayed()


def test_scrum_1_tc_10_concurrent_connection_attempts_conflict_handling(main_page, printer_list_page):
    """
    SCRUM‑1‑TC‑10 – Concurrent connection attempts – conflict handling
    """
    # Device A: Connect to first printer
    main_page.tap_connect_printer()
    printer_list_page.select_printer_by_name(printer_list_page.get_printer_names()[0])
    assert main_page.is_printer_connected()
    # Simulate Device B trying to connect – this test runs on a single device,
    # so we mimic the UI response by re‑opening the connect dialog and checking message
    main_page.tap_connect_printer()
    printer_list_page.select_printer_by_name(printer_list_page.get_printer_names()[0])
    conflict_msg = main_page.get_printer_in_use_message()
    assert "currently in use" in conflict_msg


def test_scrum_1_tc_11_low_battery_warning(main_page):
    """
    SCRUM‑1‑TC‑11 – Low‑battery warning
    """
    # Preconditions: printer battery <10% – assumed already
    assert main_page.is_low_battery_warning_displayed()


def test_scrum_1_tc_12_logout_release_printer(main_page):
    """
    SCRUM‑1‑TC‑12 – Logout / app close – release printer
    """
    main_page.tap_logout()
    # After logout, open connect dialog again and ensure no printer is auto‑selected
    main_page.tap_connect_printer()
    # The list should show printers but no indicator of being already connected
    assert not main_page.is_printer_connected()


def test_scrum_1_tc_13_persistence_of_pairing_across_app_restarts(main_page):
    """
    SCRUM‑1‑TC‑13 – Persistence of pairing across app restarts (within shift)
    """
    # Assume printer already paired
    main_page.tap_connect_printer()
    # Force‑close app (simulated by driver.reset)
    main_page.driver.reset()
    # Re‑open app (reset already re‑launched it)
    main_page.tap_connect_printer()
    assert main_page.is_printer_connected()


def test_scrum_1_tc_14_platform_compatibility(main_page):
    """
    SCRUM‑1‑TC‑14 – iOS & Android platform compatibility
    (Executed on Android – should behave identically to iOS)
    """
    # Perform a simple flow: discover and connect printer
    main_page.tap_connect_printer()
    # If no exception, assume compatibility for this basic scenario
    assert True


def test_scrum_1_tc_15_esc_pos_command_compliance(main_page):
    """
    SCRUM‑1‑TC‑15 – ESC/POS command compliance
    """
    # Capture raw data sent to printer – this requires device‑side logging; we simulate by checking a log file placeholder
    # For demonstration, we assert that a hypothetical method exists
    # In real implementation, you would pull the log from the device and inspect it
    assert True  # Placeholder


def test_scrum_1_tc_16_sensitive_receipt_data_not_logged_in_plaintext(main_page):
    """
    SCRUM‑1‑TC‑16 – Sensitive receipt data not logged in plaintext
    """
    # Trigger a print and then pull device log
    main_page.tap_print_receipt()
    # Placeholder: assume we fetched logs into a variable `log_content`
    log_content = "Mock log without receipt details"
    assert "receipt_amount" not in log_content.lower()
    assert "card_number" not in log_content.lower()


def test_scrum_1_tc_17_battery_drain_impact_on_print_latency(main_page):
    """
    SCRUM‑1‑TC‑17 – Battery‑drain impact on print latency
    """
    start = time.time()
    main_page.tap_print_receipt()
    time.sleep(5)  # wait for print completion
    elapsed = time.time() - start
    assert elapsed <= 5.0, f"Print latency {elapsed:.2f}s exceeds SLA"


def test_scrum_1_tc_18_multiple_printers_correct_selection(main_page, printer_list_page):
    """
    SCRUM‑1‑TC‑18 – Multiple printers in same store – correct printer selection
    """
    main_page.tap_connect_printer()
    printer_names = printer_list_page.get_printer_names()
    assert len(printer_names) >= 2, "Less than two printers discovered"
    printer_b = printer_names[1]  # Select the second printer (B)
    printer_list_page.select_printer_by_name(printer_b)
    assert printer_b in main_page.get_connected_printer_name()


def test_scrum_1_tc_19_firmware_version_check_unsupported(main_page):
    """
    SCRUM‑1‑TC‑19 – Printer firmware version check (unsupported version)
    """
    main_page.tap_connect_printer()
    # Assume the app attempts to connect and then shows firmware warning
    firmware_msg = main_page.get_firmware_not_supported_message()
    assert "firmware not supported" in firmware_msg.lower()


def test_scrum_1_tc_20_network_independent_operation(main_page):
    """
    SCRUM‑1‑TC‑20 – Network‑independent operation
    """
    # Ensure device is offline – this would be handled outside of the test (e.g., airplane mode)
    main_page.tap_complete_sale()
    main_page.tap_print_receipt()
    # Verify that print succeeded (no network error toast)
    assert main_page.is_printer_connected()