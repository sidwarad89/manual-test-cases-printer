import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_discoverable_printer_list_displayed(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑01 – Discoverable printer list displayed
    """
    printer_page.open_printer_connection()
    assert printer_page.wait_for_printer_list(), "Printer list was not displayed"