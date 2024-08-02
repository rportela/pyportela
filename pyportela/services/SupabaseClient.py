from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from typing import Optional
from supabase import Client, create_client


class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        path = self.path.split("?")[1] if "?" in self.path else ""
        query_params = dict(p.split("=") for p in path.split("&"))
        print("Received query params:", query_params)

        # Here, you can extract the token and do whatever you need with it

        # Send a response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Google sign-in successful! You can close this window.")


class SupabaseClient:

    supabase: Client

    def __init__(self) -> None:
        url: str = os.environ.get(
            "SUPABASE_URL", "https://cuaygngchxpwxaozhzro.supabase.co"
        )
        key: str = os.environ.get(
            "SUPABASE_KEY",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN1YXlnbmdjaHhwd3hhb3poenJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU1NTYwMjgsImV4cCI6MjAwMTEzMjAyOH0.Yp4u8akcsxJGgLWt5uRshFw3KanwXiDZpVZrttUKobI",
        )
        self.supabase = create_client(url, key)

    supabaseClient: Optional["SupabaseClient"] = None
    httpd: Optional[HTTPServer] = None

    @staticmethod
    def get_instance() -> "SupabaseClient":
        if SupabaseClient.supabaseClient is None:
            SupabaseClient.supabaseClient = SupabaseClient()
        return SupabaseClient.supabaseClient

    def table(self, name: str):
        return self.supabase.table(name)

    def start_server(self):
        server_address = ("", 8888)
        SupabaseClient.httpd = HTTPServer(server_address, RedirectHandler)
        print("Starting server at http://localhost:8888")
        SupabaseClient.httpd.serve_forever()
