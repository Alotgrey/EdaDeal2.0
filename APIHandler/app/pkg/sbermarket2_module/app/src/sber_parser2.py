import asyncio
import base64
import json
import logging
import re
from enum import Enum

import aiohttp

from APIHandler.app.pkg.sbermarket2_module.app.utils import exceptions
from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SberParser2")

class SberParser2Methods(Enum):
    GET = 'GET'
    POST = 'POST'

class SberParser2:
    def __init__(self,):
        self.email = "test"
        self.password = "test"
        self.session = None

    @staticmethod
    def get_item_data_selenium(url: str, number_market: int, fetcher: DataFetcher) -> dict:
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


    # Получить все категории магазина
    async def get_categories(self, number_market: int, prev_ver: bool = False, fetcher = None):
        if prev_ver:
            if fetcher is None:
                # Todo доделать норм вывод ошибки
                raise ValueError
            return self.get_categories_selenium(number_market=number_market, fetcher=fetcher)
        else:
            return await self.__req(
                f"https://api.sbermarket.ru/v2/taxons?sid={number_market}",
                SberParser2Methods.GET,
                {}
                )

    async def get_item_data(self, url, number_market, prev_ver: bool = False, fetcher = None):
        if prev_ver:
            if fetcher is None:
                # Todo доделать норм вывод ошибки
                raise ValueError
            return self.get_item_data_selenium(url=url, number_market=number_market, fetcher=fetcher)
        else:
            base_api_url = f"https://sbermarket.ru/api/stores/{number_market}/products/"
            item_id_api = url.split("/")[-1]
            item_url = base_api_url + item_id_api
            return await self.__req(
                item_url,
                SberParser2Methods.GET,
                {}
                )

    async def get_category_data(self, url):
        # https://sbermarket.ru/api/v3/stores/25531/categories?depth=3&include=&reset_cache=true
        raise NotImplementedError

    async def get_store(self, market_id: int, prev_ver: bool = False, fetcher = None) -> dict:
        if prev_ver:
            if fetcher is None:
                # Todo доделать норм вывод ошибки
                raise ValueError
            return self.get_store_selenium(market_id=market_id, fetcher=fetcher)

        else:
            return await self.__req(
                f"https://api.sbermarket.ru/v2/stores/{market_id}",
                SberParser2Methods.GET,
                {}
                )

    async def get_stores(self, lon: float, lat: float, prev_ver: bool = False, fetcher = None) -> dict:
        if prev_ver:
            if fetcher is None:
                # Todo доделать норм вывод ошибки
                raise ValueError
            return self.get_stores_selenium(lon=lon, lat=lat, fetcher=fetcher)

        else:
            return await self.__req(
                f"https://api.sbermarket.ru/v2/stores?lon={lon}&lat={lat}",
                SberParser2Methods.GET,
                {}
                )

    async def __req(self, url: str, method: SberParser2Methods, params: dict, headers = None, session: aiohttp.ClientSession = None):
        own_session = False
        if session is None:
            session = aiohttp.ClientSession()
            own_session = True

        if self.session is None:
            raise exceptions.AuthenticationError("Не найденно валидной сессии. Пожалуйста проверьте правильность данных и войдите заново.")

        if self.session and 'token' in self.session:
            headers = headers or {}
            headers['Authorization'] = f"Bearer {self.session['token']}"

        try:
            async with self.session.request(method.value, url, json=params, headers=headers) as response:
                response_data = await response.json()
                if response.status == 200:
                    logger.info(f"{method}::{url}=>{response.status} | result: {response_data.keys()}")
                    return await response_data
                response.raise_for_status()
        except Exception as e:
            logger.error(f"{method} :: {url}=> ", exc_info=True)
            raise e
        finally:
            if own_session:
                await session.close()
