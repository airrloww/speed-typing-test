"""
Module: test_quit_program.py

This module contains unit tests for the quit program function,
because this function needs a terminal to run and it fails on gitlab pipelines
"""

import unittest
from unittest.mock import patch
import curses
import typing_app


class TestQuitTypingApp(unittest.TestCase):
    """
    Unit tests for the functions in the typing_app module.
    """

    def test_quit_program(self):
        """
        Test if the quit_program function properly cleans up and exits the program.
        """
        with patch("sys.exit") as mock_exit, patch("curses.endwin") as mock_endwin:
            stdscr = curses.initscr()
            typing_app.quit_program(stdscr)
            mock_endwin.assert_called_once()
            mock_exit.assert_called_with(0)


if __name__ == "__main__":
    unittest.main()
