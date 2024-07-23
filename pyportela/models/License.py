from typing import Optional

from pydantic import BaseModel


class License(BaseModel):
    name: str
    url: Optional[str] = None
    description: Optional[str] = None

    def get_id(self) -> str:
        return self.name.lower()
