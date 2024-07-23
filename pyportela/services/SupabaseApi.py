from typing import Optional
import requests


class SupabaseApi:
    def __init__(self, supabase_url: str, supabase_key: str):
        self.supabase_url = supabase_url
        self.supabase_key = supabase_key

    def get(self, table_name: str, params: Optional[dict] = None):
        url = f"{self.supabase_url}/{table_name}"
        response = requests.get(
            url, headers={"apikey": self.supabase_key}, params=params
        )
        return response.json()

    def post(self, table_name: str, data: dict):
        url = f"{self.supabase_url}/{table_name}"
        response = requests.post(url, headers={"apikey": self.supabase_key}, json=data)
        return response.json()

    def put(self, table_name: str, data: dict, params: Optional[dict] = None):
        url = f"{self.supabase_url}/{table_name}"
        response = requests.put(
            url, headers={"apikey": self.supabase_key}, json=data, params=params
        )
        return response.json()

    def delete(self, table_name: str, params: Optional[dict] = None):
        url = f"{self.supabase_url}/{table_name}"
        response = requests.delete(
            url, headers={"apikey": self.supabase_key}, params=params
        )
        return response.json()
