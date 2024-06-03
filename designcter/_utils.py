import os

def bool_yesno(x: bool) -> str:
    return "Yes" if x else "No"

def dash_if_blank(x: str) -> str:
    return "-" if x == "" else x


def newlineFormatOS(text):
    """
    Adjusts the newline characters in the given text to match the operating system's format.
    
    Parameters:
    text (str): The input text with newlines.

    Returns:
    str: The text with adjusted newline characters.
    """
    if os.name == 'nt':  # Windows
        return text.replace('\n', '\r\n')
    else:  # macOS and other Unix-based systems
        return text.replace('\r\n', '\n')
