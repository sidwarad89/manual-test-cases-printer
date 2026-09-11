import pytest, time
from src.main/python/pages.printer_page import PrinterPage
from src.main/python/pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_paper_out_mid_print_error_handling(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑06 – Paper out mid‑print – error handling
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    home_page.complete_sale()
    printer_page.tap_print_receipt()
    # Simulate paper out (cannot be automated); verify error appears
    message = printer_page.get_status_message()
    assert "Paper out" in message
    # Assume user refills paper – we just retry
    printer_page.tap_print_receipt()
    # Verify receipt prints without duplicate transaction (placeholder check)
    assert "Printed" in printer_page.get_status_message()