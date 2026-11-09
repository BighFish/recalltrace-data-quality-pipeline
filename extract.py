# STEP 1: Get recall records from a sample file or the FDA API.
import json
from pathlib import Path

import requests

URL = "https://api.fda.gov/food/enforcement.json"
DATA_FOLDER = Path(__file__).parent / "data"


def extract(use_sample=True):
    DATA_FOLDER.mkdir(exist_ok=True)

    if use_sample:
        print("Using the included sample data")
        file = DATA_FOLDER / "sample_recalls.json"
        records = json.loads(file.read_text(encoding="utf-8"))
    else:
        print("Fetching data from the FDA API")
        response = requests.get(URL, params={"limit": 20}, timeout=15)
        response.raise_for_status()
        records = response.json()["results"]

    file = DATA_FOLDER / "raw_recalls.json"
    file.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"Extracted {len(records)} records")
    return records


if __name__ == "__main__":
    extract()
