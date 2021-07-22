from common import execute_api
from item_info import item_info
from search_item import search_items

APP_ID = "1019079537947262807"
FORMAT = "json"
KEYWORD = "PS5"


def test_execute_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = {
        "applicationId": APP_ID,
        "format": FORMAT,
        "keyword": KEYWORD,
    }
    result = execute_api(url, params)

    assert len(result["Items"]) >= 1
    assert result["Items"][0]["Item"]["itemCode"]


def test_search_items():
    result = search_items(KEYWORD)
    item_details = result["Items"][0]["Item"]

    assert len(result["Items"]) >= 1
    assert item_details["itemCode"]
    assert item_details["itemName"]
    assert item_details["itemPrice"]
    assert item_details["shopCode"]
    assert item_details["shopName"]
    assert item_details["itemUrl"]
