import supabase
from auth import SupabaseInstance
from cli import MetaData


class SupaBasePaperUploader:
    instance: SupabaseInstance

    def __init__(self) -> None:
        self.instance = SupabaseInstance()

    def upload_file(self, text: str, name: str):
        client: supabase.Client = self.instance.client()

        try:
            client.storage.from_("papers").upload(
                path=f"public/{name}.html",
                file=text.encode("utf-8"),
                file_options={
                    "cache-control": "3600",
                    "upsert": "False",
                    "content-type": "text/plain; charset=UTF-8",
                }
            )

        except Exception as e:
            raise RuntimeError(f"File Upload failed with error: {e}")

    def update_table(self, meta_data: MetaData):
        client: supabase.Client = self.instance.client()

        try:
            client.table("papers").insert(
                json={
                    "file": meta_data.file_name,
                    "title": meta_data.title,
                    "subject": meta_data.subject
                }
            ).execute()

        except Exception as e:
            print(f"Error while inserting record into papers table: {e}")

