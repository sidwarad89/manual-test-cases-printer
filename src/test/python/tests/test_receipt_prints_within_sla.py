import pytest, time
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_receipt_prints_within_sla(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑05 – Receipt prints within SLA
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    home_page.complete_sale()
    start = time.time()
    printer_page.tap_print_receipt()
    # Wait for success indicator
    while True:
        if "Printed" in printer_page.get_status_message():
            break
        time.sleep(0.5)
        if time.time() - start > 10:
            pytest.fail("Print did not complete within SLA")
    duration = time.time() - start
    assert duration <= 5, f"Print took {duration:.2f}s, exceeds SLA"