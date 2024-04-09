from APIHandler.app.pkg.sbermarket_module.app.sber import ItemParser, SberParser


if __name__ == "__main__":
    url = "https://sbermarket.ru/metro/drazhe-m-m-s-s-molochnym-shokoladom-80-g"

    print(ItemParser.run_item(url))
