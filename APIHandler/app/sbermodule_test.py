from pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2
from pkg.sbermarket2_module.app.utils import constants, data_fetcher
from pkg.sbermarket_module.app.categories import SberCategoriesParser
from pkg.sbermarket_module.app.sber import SberParser, itemParser


if __name__ == "__main__":
    # parser = itemParser()
    # data = parser.run_item(
    #     "https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a"
    # )
    # print(data)

    # parser.run('https://sbermarket.ru/5ka/c/myaso-ptitsa-40ebce3/vse-tovari-kategorii-cc67f80',10, 'stethem.json')
    dataFetcher = data_fetcher.DataFetcher(constants.CHROME_PATH)
    parser = SberParser2(dataFetcher)

    answer = parser.get_item_data(
        "https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a",
        324,
    )

    print(answer["product"]["name"], answer["product"]["offer"]["price"])
