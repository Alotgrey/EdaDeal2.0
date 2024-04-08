import json
import logging
import re

from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


class SberParser2:
    def __init__(self, fetcher=DataFetcher) -> None:
        self.fetcher = fetcher

    def get_item_data(self, url: str, number_market: int) -> dict:
        # https://sbermarket.ru/api/stores/64/products/batonchik-twix-minis-shokoladnyy-184-g-0cf950a
        logging.info("Начинаю получать информация по продукту")
        base_api_url = f"https://sbermarket.ru/api/stores/{number_market}/products/"

        logging.debug("Строим URL ссылку")
        item_id_api = url.split("/")[-1]
        item_url = base_api_url + item_id_api

        logging.debug("Получаем код элемента этой страницы")
        page = self.fetcher.get_page_source_code(item_url)

        logging.debug("Десериализуем строку (JSON-подобную) в словарь")
        match = re.search(r"<pre>(.*?)</pre>", page)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    def get_category_data(self, url):
        # https://sbermarket.ru/api/v3/stores/25531/categories?depth=3&include=&reset_cache=true
        raise NotImplementedError

    def get_market_data(self, ulr):
        raise NotImplementedError
