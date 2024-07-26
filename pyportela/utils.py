from collections import defaultdict
from io import BytesIO
from typing import Union
from zipfile import ZipFile

import pandas as pd


def unzip_to_df(
    zip_file: Union[str, BytesIO],
    sep: str = ",",
    dtype: Union[type, defaultdict, None] = None,
    encoding: str = "utf-8",
) -> pd.DataFrame:
    dfs = []
    with ZipFile(zip_file, "r") as zip:
        for file in zip.namelist():
            if file.lower().endswith(".csv"):
                with zip.open(file) as f:
                    df = pd.read_csv(f, sep=sep, dtype=dtype, encoding=encoding)
                    dfs.append(df)
    return pd.concat(dfs)
