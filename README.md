# RecallTrace: Beginner Python Data Engineering Project

Collect food recall records, clean them, validate them with Pydantic, check quality, and export a CSV file.

## Start here

Open this folder in VS Code. Install Python 3.10+ and run:

```bash
python -m pip install -r requirements.txt
python pipeline.py
```

By default, the pipeline uses **fictional sample records** from `data/sample_recalls.json` so it works without internet.

To retrieve live FDA records instead, edit `pipeline.py` and change `USE_SAMPLE = True` to `USE_SAMPLE = False`.

## One file at a time

| Order | File | What it does |
| --- | --- | --- |
| 1 | `extract.py` | Reads sample data or fetches 20 records from the API; stores raw JSON |
| 2 | `transform.py` | Keeps six useful fields, removes extra spaces |
| 3 | `models.py` | Defines a valid recall using Pydantic |
| 4 | `validate.py` | Accepts/rejects records according to the Pydantic model |
| 5 | `quality.py` | Removes duplicate recall numbers and impossible report dates |
| 6 | `save.py` | Exports the finished records to CSV |
| 7 | `pipeline.py` | Runs steps 1–6 in order |
| 8 | `async_extract.py` | **Optional:** fetches three API pages concurrently with asyncio + HTTPX |
| 9 | `threads.py` | **Optional:** reads multiple JSON files using threads |
| 10 | `tests/test_project.py` | Small offline tests using pytest |

Run the individual steps in order if you prefer:

```bash
python extract.py
python transform.py
python validate.py
python quality.py
python save.py
```

Run optional scripts **after** `pipeline.py`:

```bash
python async_extract.py
python threads.py
python -m pytest -q
```

## Output files

Generated automatically in `data/`:

- `raw_recalls.json`: original API/sample records
- `cleaned_recalls.json`: records with selected fields and trimmed spaces
- `valid_recalls.json` and `rejected_recalls.json`: Pydantic outcomes
- `quality_report.json`: duplicate/date checks
- `final_recalls.json` and `final_recalls.csv`: final analysis-ready records

## How the quality rules work

- Pydantic rejects missing/empty required fields and unexpected classes.
- Pydantic checks that report dates have 8 digits.
- `quality.py` separately checks that report dates are real calendar dates and eliminates repeated recall numbers.
- An FDA report can legitimately have the classification `Not Yet Classified`; it is not considered invalid.
- Duplicate handling in this project is for learning. A real system may need to retain changes to an existing recall over time.

## Data source

FDA openFDA Food Enforcement API: https://open.fda.gov/apis/food/enforcement/

The API contains historical enforcement reports and is updated periodically. **Do not use this project as a consumer safety alert system.**

## Notes

- The sample data is **fictional** and intentionally includes bad records to demonstrate validation.
- `async_extract.py` is a learning demonstration that writes a separate output file; it does not replace the main extraction step.
- `threads.py` demonstrates syntax for I/O-bound work, not that threads are necessarily faster for tiny files.
- Network requests can fail; rerun later or use sample mode.
