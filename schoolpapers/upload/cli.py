from dataclasses import dataclass
import sys


HELP_TEXT = """\
StackEdit Paper Uploader
========================

Parse a Markdown (.md) paper using StackEdit and upload the generated HTML
to the schoolpapers.org Supabase instance.

Requirements:
  - The Supabase API secret key must be set in the environment variable:
      SUPABASE_KEY

What this tool does:
  - Parses the provided Markdown paper
  - Generates HTML using StackEdit formatting
  - Uploads the file to Supabase
  - Updates the lessons table with the corresponding metadata

Usage:
  py main.py <paper.md>

Arguments:
  <paper.md>    Path to the Markdown paper to upload
"""

def parse_args() -> str | None:
    if len(sys.argv) == 2 and "--help" in sys.argv[-1]:
        print(HELP_TEXT)

    elif len(sys.argv) == 2:
        alleged_path = sys.argv[-1]

        try:
            data = parse_file(alleged_path)
            return data

        except OSError as e:
            print(f"Error opening '{alleged_path}': {e}")

    else:
        print("Command not recognized, run --help for more information")
    
    return None

def parse_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

@dataclass
class MetaData:
	file_name: str
	title: str
	subject: str

def get_subject(subjects: list[str]) -> str:
    print("\nAvailable subjects:")
    for i, subject in enumerate(subjects):
        print(f"  {i}: {subject}")

    while True:
        choice = input("\nChoose a subject by number: ").strip()
        if not choice.isdigit():
            print("Input must be a number.")
            continue

        index = int(choice)
        if index < 0 or index >= len(subjects):
            print(f"Number must be between 0 and {len(subjects) - 1}.")
            continue

        return subjects[index]


def germanize(s: str) -> str:
    table = str.maketrans({
        "ä": "ae", "ö": "oe", "ü": "ue",
        "Ä": "Ae", "Ö": "Oe", "Ü": "Ue",
    })
    return s.translate(table)


def get_meta_data(subjects: list[str]):
    while True:
        print("="*40)
        print(" Enter Paper Information ")
        print("="*40)

        subject = get_subject(subjects)
        title   = input("\nEnter the title of the paper: ").strip()

        # Construct a safe file name
        file_name = f"{germanize(subject).lower()}_{germanize(title).lower()}"
        file_name = "".join(file_name.split())  # remove spaces

        print("\nSummary of input:")
        print(f"  Title       : {title}")
        print(f"  Subject     : {subject}")
        print(f"  File Name   : {file_name}")

        confirmation = input("\nIs this correct? [y/N]: ").strip().lower()
        if confirmation == 'y':
            return MetaData(file_name=file_name, title=title, subject=subject)
        else:
            print("\nLet's try again.\n")
