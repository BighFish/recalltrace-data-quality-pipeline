# STEP 3: Check that records have the required information.
import json
from pathlib import Path

from pydantic import ValidationError
from models import Recall

DATA_FOLDER = Path(__file__).parent / "data"


def validate():
    file = DATA_FOLDER / "cleaned_recalls.json"
    records = json.loads(file.read_text(encoding="utf-8"))

    valid = []
    rejected = []

    for record in records:
        try:
            recall = Recall.model_validate(record)
            valid.append(recall.model_dump())
        except ValidationError as error:
            rejected.append({"record": record, "reason": str(error)})

    (DATA_FOLDER / "valid_recalls.json").write_text(
        json.dumps(valid, indent=2), encoding="utf-8"
    )
    (DATA_FOLDER / "rejected_recalls.json").write_text(
        json.dumps(rejected, indent=2), encoding="utf-8"
    )

    print(f"Pydantic: {len(valid)} valid, {len(rejected)} rejected")
    return valid


if __name__ == "__main__":
    validate()
