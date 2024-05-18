import asyncio
import logging
import time

from APIHandler.app.pkg.sbermarket_store_parser.parser.enums import Stores
from APIHandler.app.pkg.sbermarket_store_parser.parser.sbermarket_store_parser import (
    SbermarketStoreParser,
)


logging.basicConfig(level=logging.INFO)

async def main():
    store_parser = await SbermarketStoreParser().create(store=Stores.MAGNIT)
    result = await store_parser.run()
    print(result[:5])
    print(len(result))

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    logging.info(f"Время работы парсинга составило {(time.time() - start_time):.2f} сек.")
