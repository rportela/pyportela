import os
from typing import Optional
from supabase import Client, create_client


class SupabaseClient:

    supabase: Client

    def __init__(self) -> None:
        url: Optional[str] = os.environ.get("SUPABASE_URL")
        key: Optional[str] = os.environ.get("SUPABASE_KEY")
        if not url:
            raise ValueError("Please add SUPABASE_URL to your configuration.")
        if not key:
            raise ValueError("Please add SUPABASE_KEY to your configuration.")
        self.supabase = create_client(url, key)

    supabaseClient: Optional["SupabaseClient"]

    @staticmethod
    def get_instance() -> "SupabaseClient":
        if SupabaseClient.supabaseClient is None:
            SupabaseClient.supabaseClient = SupabaseClient()
        return SupabaseClient.supabaseClient

    def table(self, name: str):
        return self.supabase.table(name)
