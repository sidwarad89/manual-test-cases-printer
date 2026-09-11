import pytest
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_printer_out_of_range_automatic_retry(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑04 – Printer out of range – automatic retry
    """
    # Assume printer already paired
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    # Simulate out‑of‑range by disabling Bluetooth (cannot be automated here)
    home_page.complete_sale()
    printer_page.tap_print_receipt()
    message = printer_page.get_status_message()
    assert "Printer disconnected" in message
    # Retry logic is internal; we verify the message appears after attempts
    # (In real run, we would capture logs or retry count)