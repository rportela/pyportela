import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional

from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class SupabaseClient:

    supabase: Client

    def __init__(self, api_key: str) -> None:
        url: str = os.environ.get(
            "SUPABASE_URL", "https://cuaygngchxpwxaozhzro.supabase.co"
        )
        key: str = os.environ.get(
            "SUPABASE_KEY",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN1YXlnbmdjaHhwd3hhb3poenJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU1NTYwMjgsImV4cCI6MjAwMTEzMjAyOH0.Yp4u8akcsxJGgLWt5uRshFw3KanwXiDZpVZrttUKobI",
        )
        self.supabase = create_client(
            url, key, ClientOptions(headers={"apikey": api_key})
        )

    def table(self, name: str):
        return self.supabase.table(name)
