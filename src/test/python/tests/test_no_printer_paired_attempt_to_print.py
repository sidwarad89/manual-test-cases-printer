import pytest
from src.main.python.pages.printer_page import PrinterPage
from src.main.python.pages.home_page import HomePage


@pytest.mark.usefixtures("printer_page", "home_page")
def test_no_printer_paired_attempt_to_print(printer_page: PrinterPage, home_page: HomePage):
    """
    SCRUM‑1‑TC‑03 – No printer paired – attempt to print
    """
    home_page.complete_sale()
    printer_page.tap_print_receipt()
    message = printer_page.get_status_message()
    assert "No printer connected" in message
    assert printer_page.is_displayed(printer_page.RECONNECT_BTN)