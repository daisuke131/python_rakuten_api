import os
from datetime import datetime

import pandas as pd

from common import execute_api

RAKUTEN_ITEM_SEARCH_URL = (
    "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
)
APP_ID = "1019079537947262807"

WRITE_CSV_PATH = os.path.join(os.getcwd(), "csv/search_{keyword}_{datetime}.csv")


def search_items(keyword: str):
    url = RAKUTEN_ITEM_SEARCH_URL
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "keyword": keyword,
    }
    result = execute_api(url, params)
    df = pd.DataFrame()
    for item_data in result["Items"]:
        item_details = item_data["Item"]
        df = df.append(
            {
                "itemCode": item_details["itemCode"],
                "itemName": item_details["itemName"],
                "itemPrice": item_details["itemPrice"],
                "shopCode": item_details["shopCode"],
                "shopName": item_details["shopName"],
                "itemUrl": item_details["itemUrl"],
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
    search_items(keyword)
