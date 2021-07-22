import os
from datetime import datetime
from pathlib import Path

import pandas as pd

from common import execute_api

dir = Path(os.path.join(os.getcwd(), "csv"))
dir.mkdir(parents=True, exist_ok=True)

RAKUTEN_RANKING_URL = (
    "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
)
APP_ID = "1019079537947262807"
WRITE_CSV_PATH = os.path.join(os.getcwd(), "csv/info_{genere_id}_{datetime}.csv")


def ranking(genere_id: str, is_csv_output: bool):
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "genereId": genere_id,
    }
    result = execute_api(RAKUTEN_RANKING_URL, params)

    if is_csv_output:
        df = pd.DataFrame()
        for item in result["Items"]:
            item_details = item["Item"]
            df = df.append(
                {
                    "rank": item_details["rank"],
                    "itemName": item_details["itemName"],
                    "itemPrice": item_details["itemPrice"],
                    "itemUrl": item_details["itemUrl"],
                },
                ignore_index=True,
            )
        df.to_csv(
            WRITE_CSV_PATH.format(
                genere_id=genere_id,
                datetime=datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
            ),
            index=False,
            encoding="utf-8-sig",
        )
    return result


if __name__ == "__main__":
    genere_id = input("ジャンルIDを入力してください >>> ")
    ranking(genere_id)
