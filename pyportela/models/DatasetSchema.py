from typing import List, Optional
from pydantic import BaseModel
from pyportela.models.TableSchema import TableSchema


class DatasetSchema(BaseModel):

    name: str
    tables: List[TableSchema] = []
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    license: Optional[str] = None
