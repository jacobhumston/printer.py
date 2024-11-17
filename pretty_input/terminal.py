#########################
# Author: Jacob Humston #
# Date: 11/16/2024      #
# License: MIT          #
# @src/terminal.py      #
#########################

import os

def get_size() -> tuple[int, int]:
    """
    Get the size of the terminal window.
    - Returns: `tuple[int, int]` - The number of rows and columns in the terminal window.
    """
    rows, columns = os.get_terminal_size()
    return rows, columns

def clear() -> None:
    """Clear the terminal window."""
    os.system('cls' if os.name == 'nt' else 'clear')