from sbermarket2_module.app.data_fetcher import DataFetcher
from sbermarket2_module.app.constants import CHROME_PATH

import logging
import time
import re
import json


class SberParser2():
    def __init__(self) -> None:
        self.fetcher = DataFetcher(CHROME_PATH)
        

        
        
    def get_item_data(self, url: str, number_market: int) -> dict:
        # https://sbermarket.ru/api/stores/64/products/batonchik-twix-minis-shokoladnyy-184-g-0cf950a
        logging.info('Начинаю получать информация по продукту')
        base_api_url = f"https://sbermarket.ru/api/stores/{number_market}/products/"
        
        # Строим URL ссылку
        item_id_api = url.split("/")[-1]
        item_url = base_api_url + item_id_api
        
        # Запускаем Selenium
        self.driver = self.fetcher.get_driver()
        self.driver.get(item_url)
        #time.sleep(0.25)
        # Забираем ВЕСЬ код страницы
        page = self.driver.page_source
        self.driver.quit()
        
        # Десериализуем строку (JSON-подобную) в словарь
        match = re.search(r'<pre>(.*?)</pre>', page)
        pre_text = match.group(1)
        json_data = json.loads(pre_text)
        
        return json_data
    
    def get_category_data(url):
        #https://sbermarket.ru/api/v3/stores/25531/categories?depth=3&include=&reset_cache=true
        ...
        
    # def get_market_data(ulr):
    #     ...
    
    
if __name__ == '__main__':
    parser = SberParser2()
    answer = parser.get_item_data("https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a", 324)
    
    print(answer['product']['name'], answer['product']['offer']['price'])