import collections

HEADERS = (
    'Name',
    'Price',
    'Volume',
    'URL',
    'Picture',

)

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'name',
        'price',
        'volume',
        'url',
        'picture',
    )
)


SESSIONHEADERS = {
            "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.105 Safari/537.36",
            # "Referer": "https://sbermarket.ru/5ka/c/moloko-sir-yajtsa-rastitelnie-produkti-c44b0ed/moloko-ff6a59e",
            "Sec-Fetch-Mode": "cors",
            "Accept": "application/json, text/plain, */*"
        }

RETAILERS_LIST_PATH = r"sbermarket_module/app/retailers_list.txt"