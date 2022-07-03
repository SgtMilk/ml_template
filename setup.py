# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
Python script to setup the repo. Will download the necessary source data.
"""

from src.data.download import download
from src.data.clean import clean

if __name__ == "__main__":
    download()
    print("\nCleaning data...")
    clean()
