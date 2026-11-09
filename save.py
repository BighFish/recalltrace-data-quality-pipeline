# STEP 5: Export clean records as a CSV spreadsheet.
import csv
import json
from pathlib import Path

DATA_FOLDER = Path(__file__).parent / "data"


def save_csv():
    file = DATA_FOLDER / "final_recalls.json"
    records = json.loads(file.read_text(encoding="utf-8"))

    if not records:
        print("No records to save")
        return

    file = DATA_FOLDER / "final_recalls.csv"
    with file.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print(f"Saved {len(records)} records to {file.name}")


if __name__ == "__main__":
    save_csv()
