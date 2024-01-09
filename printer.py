##################################
# Printer Module
# Created by Jacob Humston
# --------------------------------
# Provides better input and
# color methods! :D
##################################

# Import modules.
import os
import colorama

# Define some color variables.
_RESET, _RED, _BLUE, _GREEN, _YELLOW, _MAGENTA = (
    colorama.Style.RESET_ALL,
    colorama.Fore.RED,
    colorama.Fore.BLUE,
    colorama.Fore.GREEN,
    colorama.Fore.YELLOW,
    colorama.Fore.MAGENTA,
)

# Define color type.
type color = red | blue | green | yellow | magenta

# This function clears the console.
def clearConsole() -> None:
    "Clear the console."
    os.system("cls" if os.name == "nt" else "clear")
    return None


# This function returns the string x amount of times.
def dupString(string: str, amount: int) -> str:
    "Get a string with `string` duplicated `amount` of times."
    newStr = ""
    for _ in range(amount):
        newStr = f"{newStr}{string}"
    return newStr


# Get the length of a string without the colors included, also fixes lines.
def colorFixedLen(string: str) -> int:
    "Get the fixed length of a string. (Supports multiple lines.)"
    # Kinda funny how simple it is, lol.
    lines = (
        string.replace(_RED, "")
        .replace(_BLUE, "")
        .replace(_GREEN, "")
        .replace(_YELLOW, "")
        .replace(_MAGENTA, "")
        .replace(_RESET, "")
        .split("\n")
    )
    return len(max(lines, key=len))


# Function to create a text bubble.
def createTextBubble(
    text: str, label: str | None = None, colorOverride: color | None = None
) -> str:
    "Create a text bubble."

    color = green
    if colorOverride != None:
        color = colorOverride

    line = color.replace(dupString("─", colorFixedLen(text) + 2), "─")
    side = color.replace("│", "│")
    corner1 = color.replace("╭", "╭")
    corner2 = color.replace("╮", "╮")
    corner3 = color.replace("╯", "╯")
    corner4 = color.replace("╰", "╰")
    labelIsBigger = False

    if label != None:
        if colorFixedLen(line) < colorFixedLen(label) + 3:
            line = color.replace(dupString("─", colorFixedLen(label) + 3), "─")
            labelIsBigger = True

    lines = text.split("\n")
    for index, part in enumerate(lines):
        lines[
            index
        ] = f"{side} {part}{dupString(' ', colorFixedLen(text) + 1 - colorFixedLen(part))}{side}"
        if label != None:
            if labelIsBigger == True:
                lines[
                    index
                ] = f"{side} {part}{dupString(' ', colorFixedLen(label) + 2 - colorFixedLen(part))}{side}"

    if label != None:
        label = color.replace(label, label)
        line2 = color.replace(
            dupString("─", (colorFixedLen(text) - colorFixedLen(label) - 3) + 2), "─"
        )
        line2Part = color.replace("─", "─")

        return f"{corner1}{line2Part} {label} {line2}{corner2}\n{f'\n'.join(lines)}\n{corner4}{line}{corner3}"
    else:
        return (
            f"{corner1}{line}{corner2}\n{f'\n'.join(lines)}\n{corner4}{line}{corner3}"
        )


# Function to create a warning text bubble.
def createWarningBubble(text: str) -> int:
    "Create a text bubble."
    return createTextBubble(text, "Warning", yellow)


# This function creates a better looking input dialog.
def betterInput(question: str, label: str | None = None) -> str:
    "Get input from the console."
    clearConsole()

    providedInput = input(
        f"{createTextBubble(question, label).replace('╰', '├')}\n{green.replace('│>', '│>')} "
    )

    clearConsole()

    return providedInput


# This function is the same as betterInput but the result will always be a int.
def betterInputInt(
    question: str, label: str | None = None, warning: str | None = None
) -> int:
    "Get input from the console. (Result will always be an int.)"
    clearConsole()

    if warning != None:
        print(createWarningBubble(warning))

    result = input(
        f"{createTextBubble(question, label).replace('╰', '├')}\n{green.replace('│>', '│>')} "
    )

    clearConsole()

    if result.isnumeric():
        return int(result)
    else:
        return betterInputInt(
            question, label, f"{red.replace(result, result)} is not a valid integer!"
        )


# This function is the same as betterInput but the result will always be a float.
def betterInputFloat(
    question: str, label: str | None = None, warning: str | None = None
) -> float:
    "Get input from the console. (Result will always be a float.)"
    clearConsole()

    if warning != None:
        print(createWarningBubble(warning))

    result = input(
        f"{createTextBubble(question, label).replace('╰', '├')}\n{green.replace('│>', '│>')} "
    )

    clearConsole()

    # Floats don't have a string method so we will use the classic try and catch.
    isFloat = True
    try:
        float(result)
    except:
        isFloat = False

    if isFloat == True:
        return float(result)
    else:
        return betterInputFloat(
            question, label, f"{red.replace(result, result)} is not a valid float!"
        )


# This function provides options, always returns a valid option number. (Starts at 0.)
def betterInputOptions(
    question: str,
    options: list[str],
    label: str | None = None,
    warning: str | None = None,
) -> int:
    "Get input from the console. (Result will always be an option number. (1+))"
    clearConsole()

    if warning != None:
        print(createWarningBubble(warning))

    stringOptions = list(options)
    for index, option in enumerate(options):
        numberString = magenta.replace(str(index + 1), str(index + 1))
        stringOptions[index] = f"{numberString}{magenta.replace(')', ')')} {option}"

    result = input(
        f"{createTextBubble(f'{question}\n{createTextBubble('\n'.join(stringOptions), 'Options', magenta)}', label).replace(green.replace('╰', '╰'), green.replace('├', '├'))}\n{green.replace('│>', '│>')} "
    )

    clearConsole()

    if result.isnumeric() and int(result) > 0 and int(result) <= len(options):
        return int(result)
    else:
        return betterInputOptions(
            question,
            options,
            label,
            f"{red.replace(result, result)} is not a valid option!\nPlease provide a number between {magenta.replace('1', '1')} and {magenta.replace(str(len(options)), str(len(options)))}.",
        )


# Input method that requires any key to continue.
def betterInputPressEnterToContinue(
    statement: str, label: str | None = None, color: color | None = None
) -> None:
    "Create an input bubble that only expects the ENTER key to be pressed."

    clearConsole()

    setColor = green
    if color != None:
        setColor = color

    input(
        f"{createTextBubble(statement, label, setColor)}\n{setColor.replace('Press ENTER to continue...', 'Press ENTER to continue...')} "
    )

    clearConsole()
    return None


# Class for coloring specific parts of a string.
class colorReplacer:
    "String color replacer class."

    def _REPLACE(string: str, replacer: str, color: str) -> str:
        "Internal replace method."
        return string.replace(replacer, f"{color}{replacer}{_RESET}")

    def red(string: str, replacer: str) -> str:
        "Color parts of a string red."
        return colorReplacer._REPLACE(string, replacer, _RED)

    def blue(string: str, replacer: str) -> str:
        "Color parts of a string blue."
        return colorReplacer._REPLACE(string, replacer, _BLUE)

    def green(string: str, replacer: str) -> str:
        "Color parts of a string green."
        return colorReplacer._REPLACE(string, replacer, _GREEN)

    def yellow(string: str, replacer: str) -> str:
        "Color parts of a string yellow."
        return colorReplacer._REPLACE(string, replacer, _YELLOW)

    def magenta(string: str, replacer: str) -> str:
        "Color parts of a string magenta."
        return colorReplacer._REPLACE(string, replacer, _MAGENTA)


# Color class.
class red:
    "Red color class."
    replace = colorReplacer.red


# Color class.
class blue:
    "Blue color class."
    replace = colorReplacer.blue


# Color class.
class green:
    "Green color class."
    replace = colorReplacer.green


# Color class.
class yellow:
    "Yellow color class."
    replace = colorReplacer.yellow


# Color class.
class magenta:
    "Magenta color class."
    replace = colorReplacer.magenta
