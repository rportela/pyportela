from typing import List, Optional
from pydantic import BaseModel
from pyportela.models.License import License
from pyportela.models.Organization import Organization
from pyportela.models.TableSchema import TableSchema


class Dataset(BaseModel):

    organization: Organization
    license: License
    name: str
    tables: List[TableSchema] = []
    description: Optional[str] = None
    tags: Optional[List[str]] = None
