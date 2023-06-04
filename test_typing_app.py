"""
Module: test_typing_app.py

This module contains unit tests for the functions in the typing_app module.
"""

import unittest
from unittest.mock import patch, mock_open, MagicMock
import typing_app


class TestTypingApp(unittest.TestCase):
    """
    Unit tests for the functions in the typing_app module.
    """

    def test_load_text(self):
        """
        Test if the load_text function correctly loads the content from a file.
        """
        file_content = "This is a test file."
        with patch("builtins.open", mock_open(read_data=file_content)):
            result = typing_app.load_text()
            self.assertEqual(result, file_content)

    def test_main(self):
        """
        Test if the main function properly calls the start_screen function.
        """
        stdscr_mock = MagicMock()

        with patch("typing_app.start_screen") as mock_start_screen:
            typing_app.main(stdscr_mock)
            mock_start_screen.assert_called_once_with(stdscr_mock)


if __name__ == "__main__":
    unittest.main()
