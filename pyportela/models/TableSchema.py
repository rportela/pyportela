from typing import List, Optional

from pydantic import BaseModel

from pyportela.models.TableSchemaColumn import DatasetTableColumn
from pyportela.utils import validate_name


class DatasetTable(BaseModel):
    organization_id: str
    name: str
    columns: List[DatasetTableColumn] = []
    primary_key: Optional[List[str]] = None
    unique_constraint: Optional[List[str]] = None
    description: Optional[str] = None

    def __init__(
        self,
        organization_id: str,
        name: str,
        columns: List[DatasetTableColumn] = [],
        primary_key: Optional[List[str]] = None,
        unique_constraint: Optional[List[str]] = None,
        description: Optional[str] = None,
    ) -> None:
        super().__init__(
            organization_id=organization_id,
            name=name,
            columns=columns,
            primary_key=primary_key,
            unique_constraint=unique_constraint,
            description=description,
        )
        validate_name(self.name)

    def get_id(self):
        return f"{self.organization_id}__{self.name}".lower()
