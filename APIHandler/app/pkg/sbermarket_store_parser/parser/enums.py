from enum import Enum


class Stores(Enum):
    MAGNIT = {'slug': 'magnit', 'id': 7217}
    PYATOROCHKA = {'slug': '5ka', 'id': 27162}
    PEREKRESTOK = {'slug': 'perekrestok', 'id': 25381}  # В Саратове нет доставки Перекрёстка, взял из Питера :)
    LENTA = {'slug': 'lenta', 'id': 357}
    METRO = {'slug': 'metro', 'id': 188}
    AUCHAN = {'slug': 'auchan', 'id': 279}