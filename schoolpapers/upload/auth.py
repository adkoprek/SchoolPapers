import os
from typing import cast
from supabase import create_client, Client
from supabase.client import ClientOptions


API_URL = "https://awxehdrpnbrixhmnnuek.supabase.co"


class SupabaseInstance:
    _connected: bool = False
    _client: Client | None = None

    def __init__(self) -> None:
        pass

    def client(self) -> Client:
        if not self._connected:
            raise RuntimeError("You first have to call: connect()")

        return cast(Client, self._client)

    @classmethod
    def _get_api_key(cls):
        env = str(os.environ.get("SUPABASE_KEY"))
        if env is None:
            raise RuntimeError("Expected a password in $SUPABASE_KEY")

        return env

    @classmethod
    def connect(cls):
        if cls._connected:
            return
        
        options = ClientOptions(postgrest_client_timeout=10, storage_client_timeout=10, schema="public")
        cls._client = create_client(API_URL, cls._get_api_key(), options)

        try:
            cls._client.storage.list_buckets()

        except:
            raise RuntimeError(f"Connecting failed")

        cls._connected = True

