import json
import logging
import re
from enum import Enum

import aiohttp

from APIHandler.app.pkg.sbermarket2_module.app.exceptions import (
    parser as parser_exception,
)
from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SberParser2")

class SberParser2Methods(Enum):
    GET = 'GET'
    POST = 'POST'


class SberParser2():
    def __init__(self, fetcher: DataFetcher = None):
        self.session = None
        self.fetcher = fetcher


    async def get_item_data(self, lon: float, lat: float, item_name: str, prev_ver: bool = False) -> dict:
        if prev_ver:
            raise NotImplementedError()
        else:
            near_markets = await self.get_stores(lon=lon, lat=lat)
            markets_mapping = {
                'ЛЕНТА': 'lenta',
                'ПЯТЕРОЧКА': '5ka',
                'МАГНИТ': 'magnit',
                'МАГНИТ СЕМЕЙНЫЙ': 'magnit',
                #'МАГНИТ СЕМЕЙНЫЙ': 'magnit_family',
                'METRO': 'metro',
                'ПЕРЕКРЕСТОК': 'crossroad',
                'АШАН': 'auchan',
            }
            # Инициализация словаря ответа
            item_data = {}
            item_data['item'] = {}
            item_data['offers'] = {market_slug:0.0 for market_slug in markets_mapping.values()}

            for market in near_markets:
                store_name = self.__parse_store_name(market['name'])
                if store_name in markets_mapping:
                    item_url = f"https://sbermarket.ru/api/v3/multicards?permalink={item_name}&store_id={market['store_id']}&tenant_id=sbermarket"
                    one_market_data = await self.__req(item_url,
                                                SberParser2Methods.GET,
                                                {}
                                                )
                    # Если у нас НЕТ полей name, description, volume и images, то собираем первичные данные, иначе - просто цену
                    if not('item' in item_data and all(k in item_data['item'] for k in ('name', 'description', 'volume', 'images'))):
                        logging.debug("Получаем первичные данные по товару")
                        item_data['item']['name'] = one_market_data['data']['product']['name']
                        item_data['item']['description'] = one_market_data['data']['product']['description']
                        item_data['item']['volume'] = str(one_market_data['data']['product']['volume']) + " " + one_market_data['data']['product']['volume_type']
                        item_data['item']['images'] = one_market_data['data']['product']['images'][0]

                    logging.debug(f"Получаем вторичные данные: цена из магазина {store_name}")
                    item_data['offers'][markets_mapping[store_name]] = one_market_data['data']['product']['offer']['price']
            return item_data


    def __parse_store_name(self, full_name):
        name_match = re.search(r"^(.*?),", full_name)
        if name_match:
            return name_match.group(1).strip()
        return None

    async def get_item_data_by_url_and_market_id(self, url, number_market, prev_ver: bool = False):
        if prev_ver:
            if self.fetcher is None:
                raise parser_exception.FetcherNotFound()
            return self.get_get_item_data_by_url_and_market_id_selenium(url=url, number_market=number_market, fetcher=self.fetcher)
        else:
            item_id_api = url.split("/")[-1]
            item_url = f"https://sbermarket.ru/api/v3/multicards?permalink={item_id_api}&store_id={number_market}&tenant_id=sbermarket"
            return await self.__req(
                item_url,
                SberParser2Methods.GET,
                {}
                )

    #TODO: Найти аналог v3
    async def get_store(self, market_id: int, prev_ver: bool = False) -> dict:
        if prev_ver:
            if self.fetcher is None:
                raise parser_exception.FetcherNotFound()
            return self.get_store_selenium(market_id=market_id, fetcher=self.fetcher)
        else:
            return await self.__req(
                f"https://api.sbermarket.ru/v2/stores/{market_id}",
                SberParser2Methods.GET,
                {}
                )

    async def get_stores(self, lon: float, lat: float, prev_ver: bool = False) -> dict:
        if prev_ver:
            if self.fetcher is None:
                raise parser_exception.FetcherNotFound()
            return self.get_stores_selenium(lon=lon, lat=lat, fetcher=self.fetcher)
        else:
            return await self.__req(
                f"https://api.sbermarket.ru/v3/stores?lon={lon}&lat={lat}",
                SberParser2Methods.GET,
                {}
                )

    @staticmethod
    def get_get_item_data_by_url_and_market_id_selenium(url: str, number_market: int, fetcher: DataFetcher) -> dict:
        # https://sbermarket.ru/api/stores/64/products/batonchik-twix-minis-shokoladnyy-184-g-0cf950a
        logging.info("Начинаю получать информация по продукту")
        base_api_url = f"https://sbermarket.ru/api/stores/{number_market}/products/"

        logging.debug("Строим URL ссылку")
        item_id_api = url.split("/")[-1]
        item_url = base_api_url + item_id_api

        logging.debug("Получаем код элемента этой страницы")
        page = fetcher.get_page_source_code(item_url)

        logging.debug("Десериализуем строку (JSON-подобную) в словарь")
        match = re.search(r"<pre>(.*?)</pre>", page)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    @staticmethod
    def get_stores_selenium(lon: float, lat: float, fetcher: DataFetcher) -> dict:
        logging.info("Начинаю получать информация по продукту")
        base_api_url = f"https://api.sbermarket.ru/v2/stores?lon={lon}&lat={lat}"

        logging.debug("Получаем код элемента этой страницы")
        page = fetcher.get_page_source_code(base_api_url)

        logging.debug("Десериализуем строку (JSON-подобную) в словарь")
        match = re.search(r"<pre>(.*?)</pre>", page)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    @staticmethod
    def get_store_selenium(market_id: int, fetcher: DataFetcher) -> dict:
        logging.info("Начинаю получать информация по продукту")
        base_api_url = f"https://api.sbermarket.ru/v2/stores/{market_id}"

        logging.debug("Получаем код элемента этой страницы")
        page = fetcher.get_page_source_code(base_api_url)

        logging.debug("Десериализуем строку (JSON-подобную) в словарь")
        match = re.search(r"<pre>(.*?)</pre>", page)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    @staticmethod
    def get_categories_selenium(number_market: int, fetcher: DataFetcher):
        logging.info("Начинаю получать информация по продукту")
        base_api_url = f"https://api.sbermarket.ru/v2/taxons?sid={number_market}"

        logging.debug("Получаем код элемента этой страницы")
        page = fetcher.get_page_source_code(base_api_url)

        logging.debug("Десериализуем строку (JSON-подобную) в словарь")
        match = re.search(r"<pre>(.*?)</pre>", page)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    async def __req(self, url: str, method: SberParser2Methods, params: dict, headers = None, session: aiohttp.ClientSession = None):
        own_session = False
        if session is None:
            session = aiohttp.ClientSession()
            own_session = True

        headers = headers or {}
        headers["api-version"] = "3.0"
        headers["client-token"] = "7ba97b6f4049436dab90c789f946ee2f"

        try:
            async with session.request(method.value, url, json=params, headers=headers) as response:
                response_data = await response.json()
                if response.status == 200:
                    logger.info(f"{method}::{url}=>{response.status}")
                    return response_data
                response.raise_for_status()
        except Exception as e:
            logger.error(f"{method}::{url}=> ", exc_info=True)
            raise e
        finally:
            if own_session:
                await session.close()
