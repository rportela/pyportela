import json
from typing import List
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.job.base import _AsyncJob
import pandas as pd


class BigQueryWarehouse:
    """BigQueryWarehouse is a class that represents a BigQuery warehouse."""

    client: bigquery.Client

    def __init__(self, credentials_json: str) -> None:
        assert credentials_json, "The credentials_json is required"
        credentials_dict = json.loads(credentials_json)
        credentials = service_account.Credentials.from_service_account_info(
            credentials_dict
        )
        self.client = bigquery.Client(
            credentials=credentials, project=credentials.project_id
        )

    def query(self, sql: str) -> bigquery.table.RowIterator:  # type: ignore
        q = self.client.query(sql)
        rows = q.result()
        return rows

    def insert(self, dataset_name: str, df: pd.DataFrame) -> _AsyncJob:
        assert df.Name, "DataFrame must have a name. It's the table name"
        table_id = f"{dataset_name}.{df.Name}"
        job = self.client.load_table_from_dataframe(
            df,
            table_id,
            job_config=bigquery.LoadJobConfig(
                autodetect=True, write_disposition="WRITE_APPEND"
            ),
        )
        return job.result()

    def merge(
        self,
        source_name: str,
        target_name: str,
        columns: List[str],
        marge_cols: List[str],
        ignore_cols: List[str] = [],
    ) -> bigquery.QueryJob:
        merge_cols_str = " AND ".join(
            f"target.{col} = source.{col}" for col in marge_cols
        )
        data_cols = [
            col for col in columns if col not in marge_cols and col not in ignore_cols
        ]
        update_sql = ", ".join(f"target.{col} = source.{col}" for col in data_cols)
        cols_sql = ", ".join(col for col in data_cols)
        sql = f"""
        MERGE INTO {target_name} AS target
        USING {source_name} AS source
        ON {merge_cols_str}
        WHEN MATCHED THEN
            UPDATE SET {update_sql}
        WHEN NOT MATCHED THEN
            INSERT ({cols_sql})
            VALUES ({cols_sql})
        """
        return self.client.query(sql)
