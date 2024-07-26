import hashlib
import os
from datetime import datetime
from io import BufferedReader
from typing import Any, Generator, Optional

import requests
from dateutil.relativedelta import relativedelta


class CachedDownload:
    folder: str

    def __init__(self, folder) -> None:
        self.folder = folder

    def get_cached_name(self, url: str) -> str:
        hash_object = hashlib.sha256(url.encode())
        hex_dig = hash_object.hexdigest()
        return os.path.join(self.folder, str(hex_dig))

    def _check_cache(
        self, cached_name: str, expiry: Optional[relativedelta] = None
    ) -> bool:
        if expiry is not None and os.path.exists(cached_name):
            tm = os.path.getmtime(cached_name)
            tm_date = datetime.fromtimestamp(tm)
            expiry_date = datetime.now() - expiry
            return tm_date > expiry_date
        else:
            return False

    def clear_cache(self, expiry: relativedelta):
        for path in self.list():
            if not self._check_cache(path, expiry):
                os.remove(path)

    def download(self, url, expiry: Optional[relativedelta] = None) -> str:
        cached_name = self.get_cached_name(url)
        if not self._check_cache(cached_name, expiry):
            os.makedirs(self.folder, exist_ok=True)
            response = requests.get(url)
            with open(cached_name, "wb") as f:
                f.write(response.content)
                f.close()
        return cached_name

    def list(self) -> Generator[str, Any, None]:
        for file in os.listdir(self.folder):
            path = os.path.join(self.folder, file)
            yield path
