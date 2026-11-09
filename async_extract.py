# STEP 7 (OPTIONAL): Fetch three API pages at the same time.
import asyncio
import json
from pathlib import Path

import httpx

URL = "https://api.fda.gov/food/enforcement.json"
DATA_FOLDER = Path(__file__).parent / "data"


async def get_page(client, skip):
    response = await client.get(URL, params={"limit": 5, "skip": skip})
    response.raise_for_status()
    return response.json()["results"]


async def main():
    async with httpx.AsyncClient(timeout=15) as client:
        pages = await asyncio.gather(
            get_page(client, 0),
            get_page(client, 5),
            get_page(client, 10),
        )

    records = []
    for page in pages:
        records.extend(page)

    DATA_FOLDER.mkdir(exist_ok=True)
    file = DATA_FOLDER / "async_recalls.json"
    file.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"Async download: {len(records)} records")


if __name__ == "__main__":
    asyncio.run(main())
