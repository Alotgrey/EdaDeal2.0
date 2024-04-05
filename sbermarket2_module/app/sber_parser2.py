from data_fetcher import DataFetcher
from constants import CHROME_PATH

import logging
import requests


class SberParser2():
    def __init__(self) -> None:
        fetcher = DataFetcher(CHROME_PATH)
        
        self.token = fetcher.get_token()
        self.cookies = fetcher.get_cookies()
        self.user_agent = fetcher.get_user_agent()
        
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'api-version': '3.0',
            'client-token': self.token,
            'User-Agent': self.user_agent
        }
        
        
    def get_item_data(self, url: str, number_market: int) -> dict:
        # https://sbermarket.ru/api/stores/64/products/batonchik-twix-minis-shokoladnyy-184-g-0cf950a
        logging.info('Начинаю получать информация по продукту')
        base_api_url = f"https://sbermarket.ru/api/stores/{number_market}/products/"
        
        item_id_api = url.split("/")[-1]
        item_url = base_api_url + item_id_api
        
        response = requests.get(url=item_url, cookies=self.cookies, headers=self.headers)
        content_json = response.json()
        # TODO: Далее он должен обработать JSON и вывести все данные
        print(content_json)
        
    
    def get_category_data(url):
        #https://sbermarket.ru/api/v3/stores/25531/categories?depth=3&include=&reset_cache=true
        ...
        
    # def get_market_data(ulr):
    #     ...
    
    
if __name__ == '__main__':
    parser = SberParser2()
    parser.get_item_data("https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a", 64)