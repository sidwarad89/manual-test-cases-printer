import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_successful_printer_connection(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑02 – Successful printer connection
    """
    printer_page.open_printer_connection()
    assert printer_page.wait_for_printer_list()
    printer_page.select_printer("EPSON_TM_P20")
    status = printer_page.get_status_message()
    assert "Printer Connected" in status, f"Unexpected status: {status}"
    assert printer_page.get_connected_printer_name() == "EPSON_TM_P20"