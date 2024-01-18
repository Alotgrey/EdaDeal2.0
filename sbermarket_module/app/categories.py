import requests
import logging
import json
import os
import datetime
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By

import constants # type: ignore
from exceptions import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('SberCategories')

class SberCategoriesParser():
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers = constants.SESSIONHEADERS
        
        response: dict = requests.get('https://sbermarket.ru/api/v3/stores/25531/categories?depth=3&include=&reset_cache=true').json()
        self.categories = response['categories']
        
        self.category_getters = {category['name']: lambda name=category['name']: self.get_category_by_name(name) for category in self.categories}
    
    def get_category_by_name(self, name: str, categories=None, lazy: bool = True) -> dict:
        """
        Ищет и возвращает категорию по её названию. Поиск может быть выполнен как в текущем списке категорий,
        так и рекурсивно в дочерних категориях.

        Параметры:
        name (str): Название категории, которую нужно найти. Поиск регистронезависимый.
        categories (list, optional): Список категорий для поиска. По умолчанию None, что означает начальный уровень поиска.
        lazy (bool, optional): Если True, поиск в дочерних категориях происходит только если название категории содержится в названии родительской категории. 
                                Если False, поиск происходит во всех дочерних категориях. По умолчанию True.

        Возвращает:
        dict: Словарь найденной категории. Если категория не найдена, возвращает пустой словарь.

        Пример использования:
        parser = SberCategoriesParser()
        bread_category = parser.get_category_by_name('Хлеб')
        """
        if categories is None:
            categories = self.categories

        for category in categories:
            # Сначала проверяем дочерние категории
            if 'children' in category and category['children']:
                if not lazy or (lazy and name.lower() in category['name'].lower()):
                    found = self.get_category_by_name(name, category['children'], lazy)
                    if found:
                        return found

            # Проверка на содержание имени категории на текущем уровне
            if name.lower() in category['name'].lower():
                return category

        return {}
    
    def get_category_slug(self, category: dict) -> str:
        """
        Возвращает slug категории.

        Параметры:
        category (dict): Словарь категории.

        Возвращает:
        str: Slug категории.
        """
        # Извлечение части URL после '/categories/'
        canonical_url = category['canonical_url']
        slug = canonical_url.split('/categories/')[-1]
        return slug
    
    def __collect_raw_json_data_for_get_retailers(self, ) -> dict:
        """
        Парсит данные с сайта через Selenium, нужные для обработки в get_retailers
        """
        url = 'https://sbermarket.ru/retailer_selection/all'
        
        logger.info(f'Инициализируем новый файл {constants.RETAILERS_LIST_PATH}')
        driver = uc.Chrome()
        
        driver.get(url)
        driver.implicitly_wait(10)    
        
        script_tag = driver.find_element(By.XPATH, '//*[@id="__NEXT_DATA__"]')
        script_content = script_tag.get_attribute('innerHTML')
        data = json.loads(script_content)
        with open(constants.RETAILERS_LIST_PATH, 'w') as file:
            json.dump(data, file)
        logger.info(f"Собрали все данные и сохранили их в {constants.RETAILERS_LIST_PATH}")
        return data
    
    def get_retailers(self) -> dict:
        """
        Возвращает список доступных ретейлеров с их идентификаторами.

        Возвращает:
        dict: Словарь, где ключи - названия ретейлеров, а значения - их идентификаторы.
        """
        # Проверка на существование файла или если файл старше 15 дней, то создаем новый
        if os.path.exists(constants.RETAILERS_LIST_PATH):
            if (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(constants.RETAILERS_LIST_PATH))).days <= 15:
                logger.warning(f'Прошло 15 дней с момента создания файла {constants.RETAILERS_LIST_PATH}. Проверьте нужно ли ему обновление!')
            logger.info(f'Нашли файл {constants.RETAILERS_LIST_PATH}. Собираем данные от туда!')
            with open(constants.RETAILERS_LIST_PATH, 'r') as file:
                data = json.load(file)
        else:
            data = self.__collect_raw_json_data_for_get_retailers()
            

        retailers_data = data['props']['pageProps']['storefrontProps']['reduxStoreState']['landing']['retailers']['entities']
        retailers = {retailer_info['name']: retailer_info['slug'] for retailer_id, retailer_info in retailers_data.items()}
        
        return retailers
    
    def get_retailer_base_url(self, retailer_name: str, category_slug: str) -> str:
        """
        Возвращает базовый URL для конкретного ретейлера и категории.

        Параметры:
        retailer_name (str): Название ретейлера.
        category_slug (str): Slug категории.

        Возвращает:
        str: Базовый URL для заданного ретейлера и категории.
        """
        retailers = self.get_retailers()
        retailer_slug = retailers.get(retailer_name)
        
        if retailer_slug:
            return f'https://sbermarket.ru/{retailer_slug}/c/{category_slug}'
        else:
            retailers_list = list(self.get_retailers().keys())
            raise BadRetailerName(f'Неверное имя ретейлера! Список разрешенных ретейлеров {retailers_list}')
    
    


        
if __name__ == '__main__':
    parser = SberCategoriesParser()
    retailers = parser.get_retailers().keys()
    print(retailers)
    