import pytest
from src.main.python.pages.printer_page import PrinterPage


@pytest.mark.usefixtures("printer_page")
def test_low_battery_warning(printer_page: PrinterPage):
    """
    SCRUM‑1‑TC‑11 – Low‑battery warning
    """
    printer_page.open_printer_connection()
    printer_page.select_printer("EPSON_TM_P20_LOW_BAT")
    # Assume printer reports low battery internally
    assert printer_page.is_low_battery_icon_visible(), "Low battery icon not shown"