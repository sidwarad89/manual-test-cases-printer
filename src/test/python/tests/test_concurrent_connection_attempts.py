import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_concurrent_connection_attempts_conflict_handling(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑10 – Concurrent connection attempts – conflict handling
    """
    # Device A connects
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    # Simulate Device B attempt (cannot be done from same driver)
    # Instead, we re‑initiate connection to emulate conflict
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    message = printer_page.get_status_message()
    assert "currently in use" in message.lower() or "queued" in message.lower()