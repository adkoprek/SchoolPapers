from typing import cast
from auth import SupabaseInstance
from cli import MetaData, get_meta_data, parse_args
from stackedit import StackeditParser
from upload import SupaBasePaperUploader
import sys


def get_subjects() -> list[str]:
    try:
        response = SupabaseInstance().client().table("subjects").select("name").execute()
        return [str(element["name"]) for element in cast(list[dict[str, str]], response.data)]

    except Exception as e:
        print(f"Error while fetching subjects: {e}")
        return []
    
if __name__ == '__main__':
    data = parse_args()
    if not data:
        sys.exit(1)

    SupabaseInstance().connect()
    meta_data: MetaData = get_meta_data(get_subjects())


    print("Parsing...")
    stackedit_parser = StackeditParser()
    stackedit_parser.insert_text(data)
    stackedit_parser.download()
    html = stackedit_parser.get_html()
    stackedit_parser.destroy()

    print("Uploading..")
    uploader: SupaBasePaperUploader = SupaBasePaperUploader()
    uploader.upload_file(html, meta_data.file_name)
    uploader.update_table(meta_data)


