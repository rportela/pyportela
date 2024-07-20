

from pydantic import BaseModel


class TableColumn(BaseModel):
    """This class represents a column of a table.
    """
    name: str
    type: str

