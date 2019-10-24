from time import time
import os
from pathlib import Path
import requests
import logging

from functools import partial
from multiprocessing.pool import Pool

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def sanitize_filename(filename):
    """Uses a blacklist to remove illegal filename characters."""
    for c in ["!", "?", "/", "\\", ":", "&"]:
        filename = filename.replace(c, "_")
    return filename


def setup_directory(directory):
    """Create a download destination directory if it doesn’t already exist.
    Returns a PosixPath instance."""
    directory = Path(directory)
    if not directory.exists():
        directory.mkdir()
    return directory


def _download(url, directory=Path("")):
    """
    Fetch a file by url and write it to a local file.
    """
    logger.info("Downloading: {0}".format(url))
    filename = sanitize_filename(os.path.basename(url))

    r = requests.get(url, stream=True)
    with (directory / filename).open("wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return str(filename)


def download(url, directory=""):
    """Wrapper for _download, that ensures directory exists."""
    ts = time()
    directory = setup_directory(directory)
    _download(url, directory)
    print("Took {}s".format(time() - ts))


def download_parallel(urls, directory="", num_processes=8):
    """Wrapper for download that uses a multiprocessing pool
    to download many files in parallel, which leads to greatly
    improved performance if the files aren't too large."""
    ts = time()
    directory = setup_directory(directory)
    with Pool(num_processes) as p:
        p.map(partial(_download, directory=directory), urls)
    print("Took {}s".format(time() - ts))


if __name__ == "__main__":
    import sys

    directory = sys.argv[1]
    files = sys.argv[2:]
    download(files[0], directory) if len(files) == 1 else download_parallel(
        files, directory
    )
