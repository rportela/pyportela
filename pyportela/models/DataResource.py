from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DataResource(BaseModel):
    dataset_id: str
    url: str
    expires: bool = False
    expires_at: Optional[datetime] = None
    downloaded_at: Optional[datetime] = None
    created_at: datetime = datetime.now()
    tags: Optional[str] = None
