import os
from datetime import datetime
from pathlib import Path

import pandas as pd

from common import execute_api

dir = Path(os.path.join(os.getcwd(), "csv"))
dir.mkdir(parents=True, exist_ok=True)

RAKUTEN_ITEM_SEARCH_URL = (
    "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
)
APP_ID = "1019079537947262807"

WRITE_CSV_PATH = os.path.join(os.getcwd(), "csv/info_{keyword}_{datetime}.csv")


def item_info(keyword: str, is_csv_output: bool):
    url = RAKUTEN_ITEM_SEARCH_URL
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "keyword": keyword,
    }
    result = execute_api(url, params)
    if is_csv_output:
        df = pd.DataFrame()
        for product in result["Products"]:
            product_details = product["Product"]
            df = df.append(
                {
                    "productName": product_details["productName"],
                    "maxPrice": product_details["maxPrice"],
                    "minPrice": product_details["minPrice"],
                    "productUrlPC": product_details["productUrlPC"],
                },
                ignore_index=True,
            )
        df.to_csv(
            WRITE_CSV_PATH.format(
                keyword=keyword, datetime=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            ),
            index=False,
            encoding="utf-8-sig",
        )
    return result
