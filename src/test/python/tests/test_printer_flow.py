import unittest
from pages.printer_page import PrinterPage
from src.test.python.tests.base_test import BaseTest

class TestPrinterExtendedFlow(BaseTest):
    """Extended flow covering multiple print actions and error handling."""

    def test_multiple_prints(self):
        printer = PrinterPage(self.driver)

        # First document
        printer.enter_document_name("Doc1.pdf")
        printer.tap_print()
        self.assertIn("Printing", printer.get_status())

        # Second document
        printer.enter_document_name("Doc2.pdf")
        printer.tap_print()
        self.assertIn("Printing", printer.get_status())

    def test_print_without_document(self):
        printer = PrinterPage(self.driver)

        # Clear any pre‑filled text (if needed)
        printer.enter_document_name("")
        printer.tap_print()

        # Expect an error status or toast – adjust the expected text based on the app.
        status = printer.get_status()
        self.assertTrue(
            any(keyword in status.lower() for keyword in ["error", "invalid", "required"]),
            f"Unexpected status for empty document: '{status}'"
        )