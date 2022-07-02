"""
This module contains functions to download data.
"""

from requests import get
from src.utils import progress_bar

BASE_PATH = "./src/data/source/"

REQUEST_LIST = [("drugcomb.csv", "https://drugcomb.fimm.fi/jing/summary_v_1_5.csv")]


def download():
    """
    Calls download_source iteratively over the `REQUEST_LIST` array.
    """
    for filename, url in REQUEST_LIST:
        download_source(filename, url)


def download_source(filename, url):
    """
    Downloads the file data from a specified url and saves it in the source folder
    with the specified file name.

    Args:
        filename (String): The file name to save the data into.
        url (String): The url where to fetch the file data from.
    """
    print(f"Downloading {filename} from {url}.")
    with get(url, stream=True) as resp:
        with open(BASE_PATH + filename, "wb") as file:
            size = int(resp.headers.get("Content-Length"))
            chunk_size = 4096
            chunk_iter = int(size / (chunk_size * 100))
            for i, chunk in enumerate(resp.iter_content(chunk_size=chunk_size)):
                file.write(chunk)
                if i % chunk_iter == 0:
                    progress_bar(i * chunk_size, size)
