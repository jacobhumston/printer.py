#######################################################
# Printer Module                                      #
# Created by Jacob Humston                            #
#                                                     #
# Util script for creating neat text bubbles,         #
# along with other things you might find helpful!     #
#                                                     #
# GITHUB: https://github.com/jacobhumston/printer.py  #
#                                                     #
# Credits to https://pastebin.com/0CMbB7EK for        #
# the custom get_key implementation.                  #
#######################################################
# NOTES:                                              #
# - RESET is considered a color.                      #
# - Naming that starts with an underscore are         #
# considered to be private.                           #
#######################################################

import os as _os
import getpass as _getpass
import sys as _sys
from typing import Literal as _Literal

if _sys.version_info[0] > 2:
    from msvcrt import getwch as _getch
else:
    from msvcrt import _getch


def get_keypress() -> str:
    "Get a keypress."
    c1 = _getch()
    if c1 in ("\x00", "\xe0"):
        arrows = {"H": "up", "P": "down", "M": "right", "K": "left"}
        c2 = _getch()
        return arrows.get(c2, c1 + c2)
    elif c1 == "\r":
        return "return"
    elif c1 == "\t":
        return "tab"
    elif c1 == "\b":
        return "backspace"
    return c1


class _OptionsCore:
    "Options used by other methods of this module."

    no_colors: bool = False
    "If true, no colors will be used. (Even when providing a color to a method.)"

    text_bubble_shape: _Literal["Round", "Square"] = "Round"
    "The shape of text bubbles."

    def set(
        self,
        name: _Literal["no_colors", "text_bubble_shape"],
        value: _Literal["Round", "Square"] | bool,
    ) -> None:
        """Optional function to modify options.
        \n`name` - Name of the option to change.
        \n`value` - New value of this option.
        """
        if type(getattr(self, name)) != type(value):
            raise Exception(
                f"Type mismatch! Expected '{type(getattr(self, name)).__name__}' but got '{type(value).__name__}'."
            )
        return setattr(self, name, value)


options = _OptionsCore()
"Options used bt other methods of this module."


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
            \n`string` - String to modify.
            \n`replacer` - Part(s) of `string` to replace with a colored variant.
            """
            if options.no_colors == True:
                return string
            return string.replace(replacer, f"{self.color}{replacer}{ColorCodes.reset}")

        def new(self, string: str) -> str:
            """Returns a colored version of `string`.
            \n`string` - String to color.
            """
            if options.no_colors == True:
                return string
            return f"{self.color}{string}{ColorCodes.reset}"

        def remove(self, string: str) -> str:
            """Removes all of this color from `string`.
            \n`string` - String to remove this color from.
            """
            return string.replace(self.color, "")

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


all_colors = [
    Colors.black,
    Colors.red,
    Colors.green,
    Colors.yellow,
    Colors.blue,
    Colors.magenta,
    Colors.cyan,
    Colors.white,
    Colors.reset,
]
"List of all colors, including reset."


def clear_console() -> None:
    "Clear the console."
    _os.system("cls" if _os.name == "nt" else "clear")
    return None


def duplicate_string(string: str, amount: int) -> str:
    """Replace all instances of `replacer` with a colored variant.
    \n`string` - String to duplicate.
    \n`amount` - Amount of times to duplicate the string.
    """
    new_string = ""
    for _ in range(amount):
        new_string = f"{new_string}{string}"
    return new_string


def remove_all_colors(string: str) -> str:
    """Removes all the colors from a string.
    \n`string` - String to remove the colors from.
    """
    for color in all_colors:
        string = color.remove(string)
    return string


def get_string_length(string: str) -> int:
    """Get the length of a string. (Supports colors and multiple lines.)
    \n`string` - The string to get the length of.
    """
    lines = remove_all_colors(string).split("\n")
    return len(max(lines, key=len))


def create_text_bubble(
    text: str,
    label: str | None = None,
    color: Colors._ColorCore = Colors.green,
    input_decorator: bool = False,
    shape: _Literal["Round", "Square"] | None = None,
) -> str:
    """Create a text bubble.
    \n`text` - The text to put inside the bubble.
    \n`label` - The label of this text bubble.
    \n`color` - The color of this text bubble.
    \n`input_decorator` - If true, an input decorator will be place at the bottom of the bubble.
    \n`shape` - Shape of the text bubble. Overrides `<options>.text_bubble_shape`.
    """

    line = color.new(duplicate_string("─", get_string_length(text) + 2))
    side = color.new("│")
    corner1 = color.new("╭")
    corner2 = color.new("╮")
    corner3 = color.new("╯")
    corner4 = color.new("╰")
    bubble = ""

    shape = shape or options.text_bubble_shape
    if shape == "Square":
        corner1 = color.new("┌")
        corner2 = color.new("┐")
        corner3 = color.new("┘")
        corner4 = color.new("└")

    label_is_bigger = False
    if label != None:
        if get_string_length(line) < get_string_length(label) + 3:
            line = color.new(duplicate_string("─", get_string_length(label) + 3))
            label_is_bigger = True

    lines = text.split("\n")
    for index, part in enumerate(lines):
        lines[
            index
        ] = f"{side} {part}{duplicate_string(' ', get_string_length(text) + 1 - get_string_length(part))}{side}"
        if label != None:
            if label_is_bigger == True:
                lines[
                    index
                ] = f"{side} {part}{duplicate_string(' ', get_string_length(label) + 2 - get_string_length(part))}{side}"

    joined_lines = '\n'.join(lines)

    if label != None:
        label = color.new(label)
        line2 = color.new(
            duplicate_string(
                "─", (get_string_length(text) - get_string_length(label) - 3) + 2
            )
        )
        line2Part = color.replace("─", "─")

        bubble = f"{corner1}{line2Part} {label} {line2}{corner2}\n{joined_lines}\n{corner4}{line}{corner3}"
    else:
        bubble = (
            f"{corner1}{line}{corner2}\n{joined_lines}\n{corner4}{line}{corner3}"
        )

    if input_decorator == True:
        return f"{bubble.replace(corner4, color.new('├'))}\n{color.new('│>')} "
    else:
        return bubble


def print_text_bubble(
    text: str,
    label: str | None = None,
    color: Colors._ColorCore = Colors.green,
    input_decorator: bool = False,
    shape: _Literal["Round", "Square"] | None = None,
) -> str:
    """Same function as `create_text_bubble` but also prints it.
    \n`text` - The text to put inside the bubble.
    \n`label` - The label of this text bubble.
    \n`color` - The color of this text bubble.
    \n`input_decorator` - If true, an input decorator will be place at the bottom of the bubble.
    \n`shape` - Shape of the text bubble. Overrides `<options>.text_bubble_shape`.
    """
    bubble = create_text_bubble(
        text=text,
        label=label,
        color=color,
        input_decorator=input_decorator,
        shape=shape,
    )
    print(bubble)
    return bubble


def create_warning_text_bubble(message: str):
    """Create a warning text bubble.
    \n`message` - The warning message.
    """
    return create_text_bubble(message, "Warning", Colors.yellow)


class _InputCore:
    "Input methods."

    class _HiddenCore:
        "Hidden input methods."

        def str(
            self,
            text: str,
            label: str | None = None,
            color: Colors._ColorCore = Colors.green,
            shape: _Literal["Round", "Square"] | None = None,
            max: int = 99999999999999,
            min: int = 1,
            warning: str | None = None,
        ) -> str:
            "Hidden input."
            current_input: str = ""
            return_pressed: int = False
            while return_pressed == False:
                clear_console()

                if warning != None:
                    print(create_warning_text_bubble(warning))

                bubble = create_text_bubble(
                    text=text,
                    label=label,
                    color=color,
                    shape=shape,
                    input_decorator=True,
                )
                print(f"{bubble}{duplicate_string('*', len(current_input))}\n")

                key = get_keypress()
                if key == "return":
                    return_pressed = True
                elif key == "backspace":
                    current_input = current_input[:-1]
                elif len(key) == 1:
                    current_input = f"{current_input}{key}"

            clear_console()

            if len(current_input) < min or len(current_input) > max:
                return self.str(
                    text=text,
                    label=label,
                    color=color,
                    shape=shape,
                    max=max,
                    min=min,
                    warning=f"Input must be between {Colors.blue.new(str(min))} and {Colors.blue.new(str(max))} characters long.",
                )

            return current_input

    hidden = _HiddenCore()
    "Hidden input methods."


input = _InputCore()
