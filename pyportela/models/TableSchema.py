

from typing import List, Optional

from pydantic import BaseModel

from pyportela.models.TableColumn import TableColumn


class TableSchema(BaseModel):
    name: str
    columns: List[TableColumn] = []
    primary_key: Optional[List[str]] = None
    unique_constraint: Optional[List[str]] = None
    description: Optional[str] = None

    