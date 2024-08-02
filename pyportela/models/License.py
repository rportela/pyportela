from typing import Optional

from pydantic import BaseModel


class License(BaseModel):
    name: str
    url: Optional[str] = None
    description: Optional[str] = None

    def __init__(
        self, name: str, url: Optional[str] = None, description: Optional[str] = None
    ) -> None:
        super().__init__(**{"name": name, "url": url, "description": description})

    def get_id(self) -> str:
        return self.name.lower()


LICENSE_CC = License(
    "CC_BY_4",
    "https://creativecommons.org/licenses/by/4.0/",
    "Creative Commons Attribution 4.0 International",
)
