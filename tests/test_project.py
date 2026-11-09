# STEP 9: Tests run without needing the real FDA API.
import pytest
from pydantic import ValidationError

from models import Recall
from quality import is_valid_date
from transform import clean_record


def test_clean_record():
    record = {"recall_number": " F-123 ", "product_description": "  Juice  "}
    result = clean_record(record)
    assert result["recall_number"] == "F-123"
    assert result["product_description"] == "Juice"


def test_valid_date():
    assert is_valid_date("20261015") is True
    assert is_valid_date("20261345") is False


def test_pydantic_rejects_missing_description():
    record = {
        "recall_number": "F-123",
        "product_description": "",
        "recalling_firm": "Example Company",
        "classification": "Class I",
        "report_date": "20261015",
    }
    with pytest.raises(ValidationError):
        Recall.model_validate(record)
