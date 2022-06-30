import sys
from requests import get
from src.utils import progress_bar

base_path = "./src/data/source/"

request_list = [("drugcomb.csv", "https://drugcomb.fimm.fi/jing/summary_v_1_5.csv")]


def download():
    for filename, url in request_list:
        download_source(filename, url)


def download_source(filename, url):
    print(f"Downloading {filename} from {url}.")
    with get(url, stream=True) as resp:
        with open(base_path + filename, "wb") as file:
            size = int(resp.headers.get("Content-Length"))
            chunk_size = 4096
            for i, chunk in enumerate(resp.iter_content(chunk_size=chunk_size)):
                file.write(chunk)
                progress_bar(i * chunk_size, size)
