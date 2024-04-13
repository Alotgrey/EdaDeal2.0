import asyncio

from APIHandler.app.pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2
from APIHandler.app.pkg.sbermarket2_module.app.utils.constants import CHROME_PATH
from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


if __name__ == "__main__":
    with DataFetcher(CHROME_PATH) as fetcher:
        parser = SberParser2()
        url = "https://sbermarket.ru/5ka/pechen-kurinaya-ptitsefabrika-severnaya-ohlazhdennaya-650-g-68be7ac"
        number_market = 235
        item_data = asyncio.run(parser.get_item_data(url=url, number_market=number_market, prev_ver=True, fetcher=fetcher))
        if item_data:
            print(item_data)


'''
Магнит = 7217
Пятерочка = 27179
Перекрёсток = ?
Лента = 715
METRO = 188
'''
