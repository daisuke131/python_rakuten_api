from common import execute_api
from search_item import search_items


def test_execute_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = {
        "applicationId": "1019079537947262807",
        "format": "json",
        "keyword": "PS5",
    }
    result = execute_api(url, params)

    assert len(result["Items"]) >= 1
    assert result["Items"][0]["Item"]["itemCode"]


def test_search_items():
    keyword = "PS5"
    result = search_items(keyword)

    assert len(result["Items"]) >= 1
    assert result["Items"][0]["Item"]["itemCode"]
    assert result["Items"][0]["Item"]["itemName"]
    assert result["Items"][0]["Item"]["itemPrice"]
