from common import execute_api

RAKUTEN_ITEM_SEARCH_URL = (
    "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
)
APP_ID = "1019079537947262807"


def search_items(keyword: str):
    url = RAKUTEN_ITEM_SEARCH_URL
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "keyword": keyword,
    }
    result = execute_api(url, params)
    return result


if __name__ == "__main__":
    keyword = input("検索ワード>>")
    search_items(keyword)
