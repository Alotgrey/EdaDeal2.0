import logging
import bs4
import csv
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants  # type: ignore

from selenium import webdriver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Sber')



class SberParser:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options)
        self.data = []
        self.result = []
        self.names_set = set()

    def load_page(self, category_url, page_number):
        url_template = f'{category_url}?page={{}}'
        url = url_template.format(page_number)
        self.driver.get(url)
        res = self.driver.page_source
        return res

    def load_item_page(self, url):
        self.driver.get(url)
        res = self.driver.page_source
        return res

    def parese_item_page(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select(
            'div.ProductDetailWrapper_root__DK_og')
        for block in container:
            try:
                self.parse_block(block=block)
            except Exception as e:
                logger.error(f'Error while parsing block: {e}')
                continue

    def parse_item_block(self, block):

        picture_block = block.select_one(
            'picture.Picture_root__5uXZZ PreviewImage_picture__xosjt')
        if not picture_block:
            logger.error('no_picture_block')
            return

        picture = picture_block.find('img')
        if not picture:
            logger.error('no_picture')
            return
        picture = picture['src']

        name_block = block.select_one('div.ProductTitle_captionContainer__1Z_Gu')
        if not name_block:
            logger.error('no_name_block')
            return

        name = name_block.select_one('h1.ProductTitle_title__aJyqe')
        if not name:
            logger.error('no_name')
            return
        name = name.text

        if name in self.names_set:
            logger.warning(f'Duplicate name: {name}. Skipping...')
            return

        price_block = block.select_one(
            'h3._Heading_1v100_1._Heading3B_1v100_36._Heading_1y7f8_29')

        #if not price_block:
         #   price_block = block.select_one('div.ProductCardPrice_price__Kv7Q7.CommonProductCard_priceText__bW6F9')
        if not price_block:
            logger.error('no_price_block')
            return
        price = price_block.text

        volume_block = block.select_one('p.ProductCTAPrice_volume__kgHsx')
        if not volume_block:
            logger.error('no_volume_block')
            return

        volume = volume_block.text

        self.result.append(constants.ParseResult(
            name=name,
            price=price,
            volume=volume,
            picture=picture,
        ))

    def run_item(self, base_url: str):
        text = self.load_item_page(base_url)
        self.parese_item_page(text=text)
        for item in self.result:
            self.data.append({
                'name': item.name,
                'price': item.price,
                'volume': item.volume,
                'picture': item.picture
            })
        json_data = json.dumps(self.data)
        return json_data

            #logger.info(f'Получено {len(self.result)} единиц продукта')
        #self.save_result(csv_save_path)
        #self.save_result_json(csv_save_path)

    def parse_page(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select(
            'div.ProductCard_root__K6IZK')
        for block in container:
            try:
                self.parse_block(block=block)
            except Exception as e:
                logger.error(f'Error while parsing block: {e}')
                continue

    def parse_block(self, block):

        url_block = block.select_one(
            'a.Link_root__fd7C0.Link_disguised__PSFAR.ProductCardLink_root__69qxV')
        if not url_block:
            logger.error('no_url_block')
            return

        url = url_block.get('href')
        if not url:
            logger.error('no_url')
            return
        url = 'https://sbermarket.ru/' + url

        name_block = block.select_one('div.ProductCard_titleContainer__5SZT1')
        if not name_block:
            logger.error('no_name_block')
            return

        name = name_block.select_one('h3.ProductCard_title__iNsaD')
        if not name:
            logger.error('no_name')
            return
        name = name.text

        if name in self.names_set:
            logger.warning(f'Duplicate name: {name}. Skipping...')
            return

        self.names_set.add(name)

        volume_block = block.select_one('div.ProductCard_volume__PINyI')
        if not volume_block:
            logger.error('no_volume_block')
            return

        volume = volume_block.text

        price_block = block.select_one(
            'div.ProductCardPrice_price__Kv7Q7.ProductCardPrice_accent__GwwRX.CommonProductCard_priceText__bW6F9')
        if not price_block:
            price_block = block.select_one('div.ProductCardPrice_price__Kv7Q7.CommonProductCard_priceText__bW6F9')
            if not price_block:
                logger.error('no_price_block')
                return

        # price = price_block.text
        # price = price_block.find('div', class_='ProductCardPrice_price__Kv7Q7')
        # if not price:
        #     logger.error('no_price')
        #     return
        for span in price_block.find_all('span'):
            span.decompose()
        price = price_block.get_text(strip=True)

        picture_block = block.select_one(
            'picture.Picture_root__5uXZZ.ProductCard_picture__lNFOz')
        if not picture_block:
            logger.error('no_picture_block')
            return

        picture = picture_block.find('img')
        if not picture:
            logger.error('no_picture')
            return
        picture = picture['src']

        # logger.info('%s, %s, %s, %s, %s',  'https://sbermarket.ru/' + url, name, volume, price, picture)

        self.result.append(constants.ParseResult(
            name=name,
            price=price,
            volume=volume,
            url=url,
            picture=picture,
        ))

        logger.debug('%s, %s, %s, %s, %s', url, name, volume, price, picture)
        logger.debug('=' * 100)

    def save_result(self, path):
        if not path.endswith('.csv'):
            path += '.csv'

        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(constants.HEADERS)
            for item in self.result:
                writer.writerow(
                    [item.name, item.price, item.volume, item.url, item.picture])

    def save_result_json(self, path):
        if not path.endswith('.json'):
            path += '.json'

        with open(path, 'w', encoding='utf-8') as f:
            json.dump([item._asdict() for item in self.result], f, ensure_ascii=False, indent=4)

    def run(self, base_url: str, num_pages: int, csv_save_path: str):
        for page_number in range(num_pages):  # КОЛВО СТРАНИЦ В КАТЕГОРИИ
            text = self.load_page(base_url, page_number)
            self.parse_page(text=text)
            logger.info(f'Получено {len(self.result)} единиц продукта')
        #self.save_result(csv_save_path)
        self.save_result_json(csv_save_path)



class itemParser:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options)
        self.data = []
        self.result = []
        self.names_set = set()

    def load_page(self, category_url, page_number):
        url_template = f'{category_url}?page={{}}'
        url = url_template.format(page_number)
        self.driver.get(url)
        res = self.driver.page_source
        return res

    def load_item_page(self, url):
        self.driver.get(url)
        res = self.driver.page_source
        return res

    def parese_item_page(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select(
            'div.ProductDetailWrapper_root__DK_og')
        for block in container:
            try:
                self.parse_item_block(block=block)
            except Exception as e:
                logger.error(f'Error while parsing block: {e}')
                continue

    def parse_item_block(self, block):

        picture_block = block.select_one(
            'picture.Picture_root__5uXZZ.PreviewImage_picture__xosjt')
        if not picture_block:
            logger.error('no_picture_block')
            return

        picture = picture_block.find('img')
        if not picture:
            logger.error('no_picture')
            return
        picture = picture['src']

        name_block = block.select_one('div.ProductTitle_captionContainer__1Z_Gu')
        if not name_block:
            logger.error('no_name_block')
            return

        name = name_block.select_one('h1.ProductTitle_title__aJyqe')
        if not name:
            logger.error('no_name')
            return
        name = name.text

        if name in self.names_set:
            logger.warning(f'Duplicate name: {name}. Skipping...')
            return

        price_block = block.select_one(
            'h3._Heading_1v100_1._Heading3B_1v100_36._Heading_1y7f8_29')

        #if not price_block:
         #   price_block = block.select_one('div.ProductCardPrice_price__Kv7Q7.CommonProductCard_priceText__bW6F9')
        if not price_block:
            logger.error('no_price_block')
            return
        price = price_block.text

        volume_block = block.select_one('p.ProductCTAPrice_volume__kgHsx')
        if not volume_block:
            logger.error('no_volume_block')
            return

        volume = volume_block.text

        self.result.append(constants.ParseItemResult(
            name=name,
            price=price,
            volume=volume,
            picture=picture,
        ))

    def run_item(self, base_url: str):
        text = self.load_item_page(base_url)
        self.parese_item_page(text=text)
        for item in self.result:
            self.data.append({
                'name': item.name,
                'price': item.price,
                'volume': item.volume,
                'picture': item.picture
            })
        json_data = json.dumps(self.data)
        print(json_data)
        return json_data