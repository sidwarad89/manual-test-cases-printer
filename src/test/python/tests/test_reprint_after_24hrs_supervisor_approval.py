import pytest
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_reprint_after_24hrs_supervisor_approval(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑09 – Re‑print after 24 hrs – supervisor approval
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    home_page.open_order_history()
    home_page.select_order("OLD_ORDER_001")  # older than 24h
    home_page.tap_reprint()
    # Supervisor PIN prompt should appear
    printer_page.enter_supervisor_pin("1234")
    printer_page.tap_print_receipt()
    assert printer_page.is_duplicate_watermark_displayed()