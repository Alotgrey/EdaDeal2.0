from categories import SberCategoriesParser
from sber import SberParser, itemParser



#!! Для корректного запуска требуется установленный Chrome на машине
if __name__ == '__main__':
    #category_parser = SberCategoriesParser()
    parser = itemParser()
    #
    # for category in category_parser.categories:
    #     base_url = category_parser.get_retailer_base_url('ПЕРЕКРЕСТОК', category_parser.get_category_slug(category))
    #     parser.run(base_url, 5, 'all_items1.json')

    parser.run_item("https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a")

    #parser.run('https://sbermarket.ru/5ka/c/myaso-ptitsa-40ebce3/vse-tovari-kategorii-cc67f80',10, 'stethem.json')