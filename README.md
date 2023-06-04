# Speed Typing Test

The Speed Typing Test is a Python program that allows users to test their typing speed by typing a given text as quickly as possible. The program provides real-time feedback on the user's typing speed in words per minute (WPM).

## Features

- Displays a welcome screen and waits for a key press to start the test.
- Randomly selects a line of text from a file as the target text for the typing test.
- Calculates the user's typing speed in WPM based on the time taken to complete the test.
- Highlights correct and incorrect characters in the target text and the user's input.
- Supports backspace/delete functionality for correcting errors during typing.
- Provides a visual indicator of the current WPM during the test.
- Allows users to repeat the test multiple times.

## Requirements

- Python 3.6 or higher
- The `curses` module (usually available by default on Unix-based systems)

## Installation

```bash
  pip install -r requirements.txt
```
 
## Usage

```bash
python3 typing_app.py

```

## Running Tests

To run tests, run the following command

```bash
  python -m unittest
```



-------------------------------------------------------------------

Type the displayed target text as quickly and accurately as possible and press enter key. Use the backspace or delete key to correct errors during typing.

Once you have completed typing the entire target text, the program will display a message indicating the completion of the test. 
Press "s" twice to play again or press the ESC key to exit the program.

Limitations
The program relies on the curses module, which may not be available or work properly on all operating systems or terminal environments.
The program assumes that the terminal or console window has sufficient width to display the entire target text.