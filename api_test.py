from common import execute_api


def test_execute_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    params = {
        "applicationId": "1019079537947262807",
        "format": "json",
        "keyword": "PS5",
    }
    result = execute_api(url, params)

    assert len(result["Items"]) >= 1
