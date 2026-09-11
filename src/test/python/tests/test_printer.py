import os
import unittest
from pages.printer_page import PrinterPage
from src.test.python.tests.base_test import BaseTest

class TestPrinterBasicFlow(BaseTest):
    """Simple test verifying that a document can be printed and status updates."""

    def test_print_single_document(self):
        printer = PrinterPage(self.driver)

        # Enter a document name (use a value from testdata if desired)
        document_name = "TestDocument.pdf"
        printer.enter_document_name(document_name)

        # Initiate printing
        printer.tap_print()

        # Verify that status label reflects the printing action
        status = printer.get_status()
        self.assertIn("Printing", status, f"Expected status to contain 'Printing', got '{status}'")