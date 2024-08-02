from collections import defaultdict
from io import BytesIO
from typing import Dict, Optional, Union
from zipfile import ZipFile

import pandas as pd
import requests


def unzip_csv(
    zip_file: Union[str, BytesIO],
    sep: str = ",",
    dtype: Union[type, defaultdict, None] = None,
    encoding: str = "utf-8",
) -> Dict[str, pd.DataFrame]:
    """
    This method unzips a zip file containing CSV files and returns a dictionary with the CSV files as DataFrames.
    The keys are the names of the files without the extension.
    """
    ds: Dict[str, pd.DataFrame] = {}
    with ZipFile(zip_file, "r") as zip:
        for file in zip.namelist():
            if file.lower().endswith(".csv"):
                key = file[:-4]
                with zip.open(file) as f:
                    df = pd.read_csv(f, sep=sep, dtype=dtype, encoding=encoding)
                    ds[key] = df
    return ds


def unzip_csv_to_df(
    zip_file: Union[str, BytesIO],
    sep: str = ",",
    dtype: Union[type, defaultdict, None] = None,
    encoding: str = "utf-8",
) -> pd.DataFrame:
    """
    Unzips a zip file containing CSV files and returns a single DataFrame with all the CSV files concatenated.
    """
    ds = unzip_csv(zip_file, sep, dtype, encoding)
    return pd.concat(ds.values(), ignore_index=True)


def download(url: str) -> BytesIO:
    """
    Downloads a file from a URL and returns it as a BytesIO object.
    """
    response = requests.get(url)
    response.raise_for_status()
    return BytesIO(response.content)


def digits_to_int(input: str) -> Optional[int]:
    """
    This function receives a string with digits and returns an integer.
    """
    digits = "".join([c for c in input if c.isdigit()])
    return int(digits) if digits else None


def validate_name(input: str) -> None:
    """
    This function validates if a name contains forbidden characters.
    """
    forbidden_chars = [".", ",", "__", " ", "-"]
    for char in forbidden_chars:
        if char in input:
            raise ValueError(f"Name cannot contain '{char}'")
