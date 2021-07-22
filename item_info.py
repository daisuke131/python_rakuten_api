import os
from datetime import datetime

import pandas as pd

from common import execute_api

RAKUTEN_ITEM_SEARCH_URL = (
    "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
)
APP_ID = "1019079537947262807"

WRITE_CSV_PATH = os.path.join(os.getcwd(), "csv/info_{keyword}_{datetime}.csv")


def item_info(keyword: str):
    url = RAKUTEN_ITEM_SEARCH_URL
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "keyword": keyword,
    }
    result = execute_api(url, params)
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


if __name__ == "__main__":
    keyword = input("検索ワード>>")
    item_info(keyword)