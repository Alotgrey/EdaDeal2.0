import asyncio

from APIHandler.app.pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2


if __name__ == "__main__":
    parser = SberParser2()

    #url = "https://sbermarket.ru/magnit_express/batonchik-twix-minis-shokoladnyy-184-g-0cf950a"
    item_name = "batonchik-twix-xtra-shokoladnyy-s-pecheniem-i-karamel-yu-82-g"
    lon = 46.020405
    lat = 51.534823

    response = asyncio.run(parser.get_item_data(lon=lon, lat=lat, item_name=item_name))
    if response:
        print(response)



'''
Магнит = 7217
Пятерочка = 27179
Перекрёсток = ?
Лента = 715
METRO = 188
'''
