
from typing import Union

from pyportela.models.DatasetSchema import DatasetSchema
from pyportela.models.TableSchema import TableSchema


class DataCatalog:
    

    def register_table(self, table: TableSchema):
        pass

    def register_dataset(self, dataset: DatasetSchema):
        pass

    def register(self, schema: Union[TableSchema, DatasetSchema]):
        if isinstance(schema, TableSchema):
            self.register_table(schema)
        pass