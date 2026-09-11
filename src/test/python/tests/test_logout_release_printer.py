import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_logout_app_close_release_printer(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑12 – Logout / app close – release printer
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20")
    printer_page.logout()
    # After logout, attempt to connect from another device would succeed
    # Here we simply verify the connection indicator cleared
    assert not printer_page.is_displayed(printer_page.CONNECTED_INDICATOR)