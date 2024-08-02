from pydantic import BaseModel


class DatasetTableColumn(BaseModel):
    """This class represents a column of a table."""

    name: str
    type: str
