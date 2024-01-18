import logging
import requests
import bs4
import csv

import constants  # type: ignore
from categories import SberCategoriesParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Sber')


class SberParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = constants.SESSIONHEADERS
        self.result = []

    def load_page(self, url_template: str, page_number: int):
        url_template += '?page={}'

        url = url_template.format(page_number)
        res = self.session.get(url=url)
        #res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select(
            'div.ProductCard_root__K6IZK.ProductCard_addToCartBig__h5PsY')
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

        volume_block = block.select_one('div.ProductCard_volume__PINyI')
        if not volume_block:
            logger.error('no_volume_block')
            return

        volume = volume_block.text

        price_block = block.select_one(
            'div.ProductCardPrice_root__OfEqa.ProductCard_price__aRuGG')
        if not price_block:
            logger.error('no_price_block')
            return

        price = price_block.find('div', class_='ProductCardPrice_price__Kv7Q7')
        if not price:
            logger.error('no_price')
            return
        for span in price.find_all('span'):
            span.decompose()
        price = price.get_text(strip=True)

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

    def run(self, base_url: str, num_pages: int, csv_save_path: str):
        for page_number in range(num_pages):  # КОЛВО СТРАНИЦ В КАТЕГОРИИ
            text = self.load_page(base_url, page_number)
            self.parse_page(text=text)
            logger.info(f'Получено {len(self.result)} единиц продукта')
        self.save_result(csv_save_path)


