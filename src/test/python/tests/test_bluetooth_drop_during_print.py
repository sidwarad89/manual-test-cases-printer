import pytest, time
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_bluetooth_drop_during_active_print_job(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑07 – Bluetooth drop during active print job
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    home_page.complete_sale()
    printer_page.tap_print_receipt()
    # Simulate Bluetooth disable (cannot be automated)
    time.sleep(1)  # wait a moment for failure
    message = printer_page.get_status_message()
    assert "Connection lost during printing" in message
    # Verify receipt status is marked as Failed (placeholder)
    assert "Failed" in message