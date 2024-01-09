##################################
# Printer Module
# Created by Jacob Humston
# --------------------------------
# Provides better input and
# color methods! :D
##################################

import os
from typing import Literal


class _OptionsCore:
    "Options used by other methods of this module."

    no_colors: bool = False
    "If true, no colors will be used. (Even when providing a color to a method.)"

    text_bubble_shape: Literal["Round", "Square"] = "Round"
    "The shape of text bubbles."


options = _OptionsCore()


class ColorCodes:
    "Terminal color codes."
    black: str = "\u001b[30m"
    "Black color code."
    
    red: str = "\u001b[31m"
    "Red color code."
    
    green: str = "\u001b[32m"
    "Green color code."
    
    yellow: str = "\u001b[33m"
    "Yellow color code."
    
    blue: str = "\u001b[34m"
    "Black color code."
    
    magenta: str = "\u001b[35m"
    "Magenta color code."
    
    cyan: str = "\u001b[36m"
    "Cyan color code."
    
    white: str = "\u001b[37m"
    "White color code."
    
    reset: str = "\u001b[0m"
    "Reset color code."


class Colors:
    "Terminal colors."

    class _ColorCore:
        "Core functionality."

        def __init__(self, color: str):
            self.color = color

        def replace(self, string: str, replacer: str) -> str:
            """Replace all instances of `replacer` with a colored variant.
            :param string: String to modify.
            :param replacer: Part(s) of `string` to replace with a colored variant.
            """
            return string.replace(replacer, f"{self.color}{replacer}{ColorCodes.reset}")

        def set(self, string: str) -> str:
            """Returns a colored version of `string`.
            :param string: String to color.
            """
            return f"{self.color}{string}{ColorCodes.reset}"

    black = _ColorCore(ColorCodes.black)
    "Black color method."

    red = _ColorCore(ColorCodes.red)
    "Red color method."

    green = _ColorCore(ColorCodes.green)
    "Green color method."

    yellow = _ColorCore(ColorCodes.yellow)
    "Yellow color method."

    blue = _ColorCore(ColorCodes.blue)
    "Blue color method."

    magenta = _ColorCore(ColorCodes.magenta)
    "Magenta color method."

    cyan = _ColorCore(ColorCodes.cyan)
    "Cyan color method."

    white = _ColorCore(ColorCodes.white)
    "White color method."

    reset = _ColorCore(ColorCodes.reset)
    "Reset color method."


type Color = Colors._ColorCore


def clear_console() -> None:
    "Clear the console."
    os.system("cls" if os.name == "nt" else "clear")
    return None

