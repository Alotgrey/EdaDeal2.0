from categories import SberCategoriesParser
from sber import SberParser

if __name__ == '__main__':
    category_parser = SberCategoriesParser()
    parser = SberParser()

    for category in category_parser.categories:
        base_url = category_parser.get_retailer_base_url('ПЕРЕКРЕСТОК', category_parser.get_category_slug(category))
        parser.run(base_url, 5, 'all_items.csv')