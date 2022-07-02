# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
This module contains functions to clean up the source data.
"""

from pandas import read_csv
from src.params import SOURCE_PATH, CLEAN_PATH, REQUEST_LIST


def clean():
    """
    This function process the dirty data from the source data folder in a
    format appropriate for our ML usage.
    """
    for filename, _ in REQUEST_LIST:
        dataframe = read_csv(
            SOURCE_PATH + filename,
            # index_col="SOMETHING HERE",
        )

        ### PROCESS DATA HERE ###

        dataframe.to_csv(CLEAN_PATH + filename)
