"""
This module contains different tools for the command line
"""

from sys import stdout

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
