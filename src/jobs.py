import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    try:
        with open(path, encoding="utf8") as file:
            jobs = csv.DictReader(file)
            return [job for job in jobs]
    except OSError:
        print("File not found")
