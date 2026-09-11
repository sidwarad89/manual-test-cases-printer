import pytest
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_reprint_same_day_duplicate_copy(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑08 – Re‑print same‑day receipt (duplicate copy)
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    home_page.complete_sale()
    printer_page.tap_print_receipt()
    # Assume receipt printed successfully
    home_page.open_order_history()
    home_page.select_order("ORDER123")
    home_page.tap_reprint()
    printer_page.tap_print_receipt()
    assert printer_page.is_duplicate_watermark_displayed(), "Duplicate watermark missing"