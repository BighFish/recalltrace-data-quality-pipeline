# The Pydantic model describes what a good record looks like.
from typing import Literal

from pydantic import BaseModel, Field


class Recall(BaseModel):
    recall_number: str = Field(min_length=1)
    product_description: str = Field(min_length=1)
    recalling_firm: str = Field(min_length=1)
    classification: Literal[
        "Class I", "Class II", "Class III", "Not Yet Classified"
    ]
    report_date: str = Field(pattern=r"^\d{8}$")
    reason_for_recall: str = ""
