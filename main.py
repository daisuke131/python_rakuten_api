from item_info import item_info
from ranking import ranking
from search_item import search_items


def main():
    api_type = input("0:search_item, 1:item_info, 2:ranking >>")
    if api_type == "2":
        genere_id = input("ジャンルID>>")
    else:
        keyword = input("検索ワード>>")
    is_csv_output = input("csv出力 0:no, 1:yes >>")

    if api_type == "0":
        search_items(keyword, bool(int(is_csv_output)))
    elif api_type == "1":
        item_info(keyword, bool(int(is_csv_output)))
    elif api_type == "2":
        ranking(genere_id, bool(int(is_csv_output)))


if __name__ == "__main__":
    main()
