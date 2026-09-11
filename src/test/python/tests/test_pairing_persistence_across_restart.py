import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_pairing_persistence_across_app_restarts(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑13 – Persistence of pairing across app restarts (within shift)
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    # Simulate app force‑close by resetting driver session
    printer_page.driver.close_app()
    printer_page.driver.launch_app()
    # Verify printer still appears as connected
    connected_name = printer_page.get_connected_printer_name()
    assert connected_name == "EPSON_TM_P20", "Paired printer not retained after restart"