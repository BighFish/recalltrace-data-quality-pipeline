# STEP 4: Find invalid dates and duplicate recall numbers.
import json
from datetime import datetime
from pathlib import Path

DATA_FOLDER = Path(__file__).parent / "data"


def is_valid_date(value):
    try:
        datetime.strptime(value, "%Y%m%d")
        return True
    except ValueError:
        return False


def quality():
    file = DATA_FOLDER / "valid_recalls.json"
    records = json.loads(file.read_text(encoding="utf-8"))

    good_records = []
    seen_numbers = set()
    duplicates = 0
    bad_dates = 0

    for record in records:
        number = record["recall_number"]

        if not is_valid_date(record["report_date"]):
            bad_dates += 1
            continue

        if number in seen_numbers:
            duplicates += 1
            continue

        seen_numbers.add(number)
        good_records.append(record)

    report = {
        "checked_records": len(records),
        "duplicate_records": duplicates,
        "invalid_dates": bad_dates,
        "ready_for_analysis": len(good_records),
    }

    (DATA_FOLDER / "final_recalls.json").write_text(
        json.dumps(good_records, indent=2), encoding="utf-8"
    )
    (DATA_FOLDER / "quality_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print("Quality report:", report)
    return good_records


if __name__ == "__main__":
    quality()
