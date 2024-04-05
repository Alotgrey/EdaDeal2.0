import undetected_chromedriver as uc
import logging
import json
import time
import re

from constants import UTILS_PATH


class DataFetcher():
    def __init__(self, browser_path) -> None:
        self.browser_path = browser_path
        try:
            self.__validate_browser_path()
        except FileNotFoundError as e:
            logging.error(f'Не корректно задан путь к браузеру Chrome в переменной browser_path={self.browser_path}')
            raise e
    
    def get_cookies(self, ) -> dict:
        cookies = self.__get_cookies_from_file()
        
        if not cookies:
            all_data = self.__get_all_data()
            cookies = all_data['cookies']
        return cookies
    
    def get_user_agent(self, ) -> str:
        user_agent = self.__get_user_agent_from_file()
        
        if not user_agent:
            all_data = self.__get_all_data()
            user_agent = all_data['user_agent']
        return user_agent
        
    def get_token(self, ) -> str:
        token = self.__get_token_from_file()
        
        if not token:
            all_data = self.__get_all_data()
            token = all_data['token']
        return token
    
    def __validate_browser_path(self):
        try:
            driver = self.__get_driver(headless=True)
            driver.quit()
        except FileNotFoundError:
            raise FileNotFoundError(f'Не найден путь к браузеру Chrome: {self.browser_path}')
    
        
    def __get_driver(self, headless=False):
        try:
            driver = uc.Chrome(headless=headless)
        except TypeError:
            driver = uc.Chrome(headless=headless, browser_executable_path=self.browser_path)
        return driver       
        
    def __get_all_data(self) -> dict:
        logging.info('Открываю браузер хром для получения токена')
        driver = self.__get_driver()
        
        driver.get('https://sbermarket.ru/')
        user_agent = driver.execute_script("return navigator.userAgent;")
        time.sleep(5)
        token = re.findall('STOREFRONT_API_V3_CLIENT_TOKEN: "([^"]+)"', driver.page_source)[0]
        cookies = driver.get_cookies()
        
        #TODO: Как будто не правильная обработка куки, сохраняется самый последний кук в списке.
        # Хотя с другой стороны нам вроде как и не нужны куки
        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie['name']] = cookie['value']
            
        driver.quit()
        logging.info(f'Токен получен: {token}')
        
        self.__save_token_in_file(token=token)
        self.__save_cookies_in_file(cookies=cookies_dict)
        self.__save_user_agent_in_file(user_agent=user_agent)
        
        return {'token': token,
                'cookies': cookies,
            'user_agent': user_agent}
        
    
    def __save_cookies_in_file(self, cookies: dict):
        """Сохраняет токен в файл"""
        with open(rf'{UTILS_PATH}\cookies.json', 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        logging.info('Куки сохранены в файл')
        
    def __save_user_agent_in_file(self, user_agent: str):
        """Сохраняет user-agent в файл"""
        with open(rf'{UTILS_PATH}\user_agent.txt', 'w', encoding='utf-8') as f:
            f.write(user_agent)
        logging.info('User_agent сохранен в файл')
    
    def __save_token_in_file(self, token: str):
        """Сохраняет токен в файл"""
        with open(rf'{UTILS_PATH}\token.txt', 'w', encoding='utf-8') as f:
            f.write(token)
        logging.info('Токен сохранен в файл')
    
    
    def __get_cookies_from_file(self) -> str | None:
        """Получить куки из файла"""
        try:
            with open(rf'{UTILS_PATH}\cookies.json', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            logging.debug('Получены куки из файла')
        except FileNotFoundError:
            logging.error('Файл с куки не найден')
            return None
            
        return cookies
    
    def __get_user_agent_from_file(self) -> str | None:
        """Получить user_agent из файла"""
        try:
            with open(rf'{UTILS_PATH}\user_agent.txt', 'r', encoding='utf-8') as f:
                user_agent = f.read()
            logging.debug('Получен user_agent из файла')
        except FileNotFoundError:
            logging.error('Файл с user_agent не найден')
            return None
        
        return user_agent
    
    def __get_token_from_file(self) -> str | None:
        """Получить токен из файла"""
        try:
            with open(rf'{UTILS_PATH}\token.txt', 'r', encoding='utf-8') as f:
                token = f.read()
            logging.debug('Получен токен из файла')
        except FileNotFoundError:
            logging.error('Файл с токеном не найден')
            return None
        
        return token
    
    
    
    
if __name__ == '__main__':
    from constants import CHROME_PATH
    test = DataFetcher(CHROME_PATH)
    cookies = test.get_cookies()
    token = test.get_token()
    
    print(cookies, token)