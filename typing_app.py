"""
This program is a Speed Typing Test implemented using the curses library in Python.
It presents the user with a target text and allows them to type it within a specified time.
After the typing is complete, it calculates the user's words per minute (WPM)
based on the accuracy and time taken.

Ensure that the 'test.txt' file exists in the same directory as the script,
and it contains the target text for the typing test.

Note: The program assumes an average word length of 5 characters to calculate WPM.
You may adjust this assumption based on your requirements.
"""

import curses
import sys
import time


def quit_program(stdscr):
    """
    Quit the program and perform cleanup.

    Args:
        stdscr (curses._CursesWindow): The curses window object.
    """
    stdscr.clear()
    stdscr.addstr("\n[+] Quitting...")
    stdscr.refresh()

    curses.napms(900)
    curses.endwin()
    sys.exit(0)


def start_screen(stdscr):
    """
    Starts the game with a countdown timer and displays the test text
    """
    stdscr.addstr("[+] Welcome to the Speed Typing Test")
    stdscr.addstr("\n[+] Press 'S' to start, press 'ESC' to quit!\n")

    while True:
        key = stdscr.getch()

        if key == ord("s"):
            display_text(stdscr)
            continue

        if key == 27:
            quit_program(stdscr)
            break


def display_text(stdscr):
    """
    Starts the game with a countdown timer and displays the test text
    """
    stdscr.clear()
    for i in range(5, 0, -1):
        stdscr.addstr(f"[+] test starts in {str(i)}\n")
        stdscr.refresh()
        stdscr.clear()
        time.sleep(1)
    wpm_test(stdscr)


def load_text():
    """
    Loads the target text from a file named "test.txt"

    Returns:
        str: the content of a txt file named test, or error in case file not found
    """
    file_path = "test.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            target_text = file.read()
        return target_text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""


def wpm_test(stdscr):
    """
    Conducts the speed typing test.

    Args:
        stdscr (curses.window): The curses window object.
    """

    stdscr.clear()
    stdscr.addstr("\n[+] Type the following text and press Enter to finish the test:")
    stdscr.refresh()

    start_time = time.time()

    target_text = load_text()
    stdscr.addstr("\n\n" + target_text)
    stdscr.refresh()

    stdscr.move(4, 0)
    input_text = ""
    delete_keys = {curses.KEY_BACKSPACE, curses.KEY_DC, 127}

    while True:
        key = stdscr.getch()

        input_text += chr(key)
        stdscr.addch(key)
        stdscr.refresh()

        if key == 27:
            quit_program(stdscr)
            break

        if key == 10:
            break

        if key in delete_keys:
            input_text = input_text[:-1]
            # pylint: disable=<C0103>
            y, x = stdscr.getyx()
            stdscr.move(y, x - 1)
            stdscr.delch()

    stdscr.addstr("\n\n[+] Your typed text:")
    stdscr.addstr("\n" + input_text)
    stdscr.refresh()

    # Calculate words per minute
    input_words = len(input_text.split())
    time_taken = time.time() - start_time
    minutes_taken = time_taken / 60.0
    wpm = input_words / minutes_taken
    stdscr.addstr(f"\n\n[+] you typed: {wpm:.2f} Words per minute")
    stdscr.refresh()

    stdscr.addstr("\n\n[+] press 's' twice to try again")
    if key == ord("s"):
        display_text(stdscr)

    stdscr.getch()


def main(stdscr):
    """
    Main function to start the Speed Typing Test application.

    Args:
        stdscr (curses._CursesWindow): The curses window object.
    """
    stdscr.clear()
    while True:
        start_screen(stdscr)
        break


if __name__ == "__main__":
    curses.wrapper(main)
