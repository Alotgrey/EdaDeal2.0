import json
import logging
import re
from typing import Dict, List, Union

import nodriver as uc
from tqdm import tqdm

from APIHandler.app.pkg.sbermarket_store_parser.db.models import Category, Product
from APIHandler.app.pkg.sbermarket_store_parser.db.queries.orm import AsyncORM
from APIHandler.app.pkg.sbermarket_store_parser.parser.enums import Stores


logging.basicConfig(level=logging.INFO)


class SbermarketStoreParser:
    def __init__(self) -> None:
        self.store: Stores = None
        self.driver: uc.Browser = None

        self.category_mapper = {}

        self.global_category_id = 0

    @classmethod
    async def create(cls, store: Stores,):
        self = cls()
        self.driver = await uc.start()
        self.store = store
        return self

    async def run(self) -> None:
        base_url = f"https://sbermarket.ru/api/v3/stores/{self.store.value['id']}/departments/"
        all_items = await self.__get_all_items(base_url)
        self.driver.stop()
        unique_categories = await self.categories_to_db(all_items)
        await self.items_to_db(all_items)
        logging.info(f'В БД было загружено {len(all_items)} предметов из {len(unique_categories)} разных категорий')

        return all_items

    async def categories_to_db(self, items: List[Dict[str, Union[str, List]]]) -> Dict:

        unique_categories = {}
        for item in items:
            category = item['category']
            if category not in unique_categories:
                unique_categories[category] = item

        for (item_category, item_data) in tqdm(unique_categories.items(), desc="Загружаем категории в БД"):
            category = Category(
                id=item_data['category_id'],
                name=item_category,
                image_url=None,
                isFinal=item_data['is_final'],
                parent_id=item_data['parent_id']
            )
            await AsyncORM.insert_item(category)
        return unique_categories

    async def items_to_db(self, items: List[Dict[str, Union[str, List]]]) -> None:
        for item in tqdm(items, desc="Загружаем предметы в БД"):
            product = Product(
                name=item['name'],
                image_url=item['img_urls'][0] if item['img_urls'] else None,
                category_id=item['category_id'],
                link=item['url']
            )
            await AsyncORM.insert_item(product)

    async def __get_all_items(self, base_url: str, slug: str='', is_final=True) -> List[Dict[str, Union[str, List]]]:
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

            all_items.extend(await self.__normalize_items_data(page_data, is_final=is_final))

            for department in page_data['departments']:
                child_slug = department['slug']
                child_items = await self.__get_all_items(base_url, slug=child_slug, is_final=False)
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

    async def __normalize_items_data(self, page_data: dict, is_final=True) -> List[Dict[str, Union[str, List]]]:
        category_items = []
        for departament in page_data['departments']:
            for products in departament['products']:

                current_slug = departament['slug']
                if self.category_mapper.get(current_slug, None) is None:
                    self.category_mapper[current_slug] = self.global_category_id
                    self.global_category_id += 1

                parent_slug = page_data.get('department', None)
                if parent_slug:
                    parent_slug = parent_slug.get('slug', None)

                item_data = {
                    'name': products.get('name', None),
                    'url': products.get('canonical_url', None),
                    'img_urls': products.get('image_urls', []),

                    'category': current_slug,
                    'category_id': self.category_mapper.get(current_slug),

                    'is_final': is_final,
                    'parent_id': self.category_mapper.get(parent_slug, None)
                }

                category_items.append(item_data)
        return category_items