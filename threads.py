# STEP 8 (OPTIONAL): Read several local JSON files with threads.
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DATA_FOLDER = Path(__file__).parent / "data"


def count_records(file):
    records = json.loads(file.read_text(encoding="utf-8"))
    return f"{file.name}: {len(records)} records"


def main():
    files = [
        DATA_FOLDER / "raw_recalls.json",
        DATA_FOLDER / "cleaned_recalls.json",
        DATA_FOLDER / "valid_recalls.json",
    ]

    with ThreadPoolExecutor(max_workers=3) as pool:
        for answer in pool.map(count_records, files):
            print(answer)


if __name__ == "__main__":
    main()
