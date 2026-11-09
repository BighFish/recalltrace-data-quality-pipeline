# STEP 2: Keep only the fields we want to analyze.
import json
from pathlib import Path

DATA_FOLDER = Path(__file__).parent / "data"


def clean_record(record):
    return {
        "recall_number": (record.get("recall_number") or "").strip(),
        "product_description": (record.get("product_description") or "").strip(),
        "recalling_firm": (record.get("recalling_firm") or "").strip(),
        "classification": (record.get("classification") or "").strip(),
        "report_date": (record.get("report_date") or "").strip(),
        "reason_for_recall": (record.get("reason_for_recall") or "").strip(),
    }


def transform():
    file = DATA_FOLDER / "raw_recalls.json"
    records = json.loads(file.read_text(encoding="utf-8"))

    cleaned = []
    for record in records:
        cleaned.append(clean_record(record))

    file = DATA_FOLDER / "cleaned_recalls.json"
    file.write_text(json.dumps(cleaned, indent=2), encoding="utf-8")
    print(f"Transformed {len(cleaned)} records")
    return cleaned


if __name__ == "__main__":
    transform()
