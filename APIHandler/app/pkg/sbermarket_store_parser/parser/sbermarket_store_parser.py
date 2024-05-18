import json
import logging
import re
from typing import Dict, List, Union

import nodriver as uc

from APIHandler.app.pkg.sbermarket_store_parser.parser.enums import Stores


# from db.session import Session
# from models import Product



logging.basicConfig(level=logging.INFO)


class SbermarketStoreParser:
    def __init__(self) -> None:
        self.store: Stores = None
        self.driver: uc.Browser = None

    @classmethod
    async def create(cls, store: Stores):
        self = cls()
        self.driver = await uc.start()
        self.store = store
        return self

    #TODO: Добавить PostgreSQL
    async def run(self) -> None:
        base_url = f"https://sbermarket.ru/api/v3/stores/{self.store.value['id']}/departments/"
        all_items = await self.__get_all_items(base_url)

        self.driver.stop()
        return all_items


    async def __get_all_items(self, base_url: str, slug: str='') -> List[Dict[str, Union[str, List]]]:
        all_items = []
        page_num = 1
        while True:
            url = base_url + slug + f"?offers_limit=100&per_page=100&page={page_num}"
            page_data = await self.__get_json(url)

            # Условие остановки
            if page_data.get('message'):
                if page_data['message'].count('category without children') > 0:
                    logging.info(f'Категория {slug} без детей |\n{url}')
                    break

            if page_data.get('departments') == []:
                logging.info(f'Пустой departments в {slug} |\n{url}')
                break

            all_items.extend(await self.__normalize_items_data(page_data))

            for department in page_data['departments']:
                child_slug = department['slug']
                child_items = await self.__get_all_items(base_url, slug=child_slug)
                all_items.extend(child_items)

            page_num += 1
        return all_items

    async def __get_json(self, url: str) -> Dict:
        page = await self.driver.get(url)
        page_content = await page.get_content()
        match = re.search(r"<pre>(.*?)</pre>", page_content)
        if match:
            pre_text = match.group(1)

            return json.loads(pre_text)
        return {}

    async def __normalize_items_data(self, page_data: dict) -> List[Dict[str, Union[str, List]]]:
        category_items = []
        for departament in page_data['departments']:
            for products in departament['products']:
                item_data = {
                    'name': products.get('name', None),
                    'url': products.get('canonical_url', None),
                    'img_urls': products.get('image_urls', []),
                    'category': None    #FIXME каким то образом мапить по категориям???
                }
                category_items.append(item_data)
        return category_items