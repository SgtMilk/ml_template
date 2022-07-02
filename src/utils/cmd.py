# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
This module contains different tools for the command line
"""

from sys import stdout
from functools import reduce

BAR_LEN = 60


def progress_bar(count, total, suffix=""):
    """
    Will print a progess bar and update it at each call.

    Args:
        count (int): progress in the total.
        total (int): the maximum the count can go to.
        suffix (str, optional): a message to add at the end of the progress bar. Defaults to "".
    """

    filled_len = int(round(BAR_LEN * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar_progress = "=" * filled_len + "-" * (BAR_LEN - filled_len)

    stdout.write(f"[{bar_progress}] {percents}%    {suffix}         \r")
    stdout.flush()


def printc(text: str, style):
    """
    This function prints a message in a certain style.

    Args:
        text (str): the text to print.
        style (list): array of styles to print in. Here are the valid inputs:
            - header
            - bold
            - underline
            - blue
            - cyan
            - green
            - yellow
            - red
            Note that some style may not be applied if they conflict or if they are not valid
    """

    color = {
        "header": "\033[95m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
    }
    endc = "\033[0m"

    style_string = reduce(lambda prev, cur: prev + color[cur] if cur in color else "", style, "")

    print(style_string + text + endc)
