from fastapi import APIRouter, HTTPException, Query

from APIHandler.app.pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2
from APIHandler.app.pkg.sbermarket2_module.app.utils.constants import CHROME_PATH
from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


router = APIRouter(prefix="/api/v2/parser")


@router.get("/item/url/")
async def get_item_data(url: str, market_id: int) -> dict:
    with DataFetcher(CHROME_PATH) as fetcher:
        parser = SberParser2()
        try:
            item_data = await parser.get_item_data(url=url, number_market=market_id, prev_ver=True, fetcher=fetcher)
            if item_data:
                return item_data
            else:
                raise HTTPException(status_code=404, detail="Item data not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@router.get("/stores/")
async def get_store(market_id: int = None, lon: float = Query(None), lat: float = Query(None)) -> dict:
    with DataFetcher(CHROME_PATH) as fetcher:
        parser = SberParser2()
        try:
            if market_id is not None:
                store_data = await parser.get_store(market_id=market_id, prev_ver=True, fetcher=fetcher)

            elif lon is not None and lat is not None:
                store_data = await parser.get_stores(lon=lon, lat=lat, prev_ver=True, fetcher=fetcher)

            if store_data:
                return store_data
            else:
                raise HTTPException(status_code=404, detail="Item data not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.get("/stores/{market_id}/categories/")
async def get_store_categories(market_id: int) -> dict:
    with DataFetcher(CHROME_PATH) as fetcher:
        parser = SberParser2()
        try:
            categories_data = await parser.get_categories(number_market=market_id, prev_ver=True, fetcher=fetcher)
            if categories_data:
                return categories_data
            else:
                raise HTTPException(status_code=404, detail="Item data not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
