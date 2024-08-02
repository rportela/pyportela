from typing import Optional
from sqlalchemy import create_engine, text
import pandas as pd


def sql_format(value, dtype: str):
    if dtype == "int":
        return str(value)
    elif dtype == "float":
        return str(value)
    elif dtype == "date":
        return value.strftime("'%Y-%m-%d'")
    elif dtype == "datetime":
        return value.strftime("'%Y-%m-%d %H:%M:%S'")
    elif dtype == "object" or dtype == "str" or dtype == "string":
        value = str(value).replace("'", "''")
        return "'" + value + "'"
    else:
        raise ValueError(f"Type {dtype} not supported")


class PostgresWarehouse:
    def __init__(self, connection_string: str) -> None:
        self.engine = create_engine(connection_string)

    def add_data(self, df: pd.DataFrame, overwrite: bool = False) -> Optional[int]:
        assert df.Name, "The DataFrame name (or table destination) is required"
        return df.to_sql(
            df.Name,
            self.engine,
            if_exists="replace" if overwrite else "append",
            index=False,
        )

    def save(
        self,
        df: pd.DataFrame,
        replace_col: Optional[str] = None,
        overwrite: bool = False,
    ) -> Optional[int]:
        if overwrite == True:
            return self.add_data(df, overwrite=True)
        if replace_col:
            unique_values = df[replace_col].unique()
            sql_values = ",".join(
                sql_format(v, df[replace_col].dtype.name) for v in unique_values
            )
            query = f"DELETE FROM {df.Name} WHERE {replace_col} IN ({sql_values})"
            self.execute(query)
        return self.add_data(df, overwrite=False)

    def execute(self, query: str):
        with self.engine.connect() as connection:
            connection.execute(text(query)).close()
            connection.close()
