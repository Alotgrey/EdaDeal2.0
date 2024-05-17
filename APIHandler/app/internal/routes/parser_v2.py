from typing import Dict, List

from fastapi import APIRouter, HTTPException

from APIHandler.app.pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2


router = APIRouter(prefix="/api/v1/sbermarket")


@router.get("/items/")
async def get_item_data_by_url_and_market_id(url: str, market_id: int) -> dict:
    parser = SberParser2()
    try:
        item_data = await parser.get_item_data_by_url_and_market_id(url=url, number_market=market_id)
        if item_data:
            return item_data
        else:
            raise HTTPException(status_code=404, detail="Item data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/items/nearby-prices/")
async def get_compared_data(lon: float, lat: float, item_name: str) -> dict:
    parser = SberParser2()
    try:
        item_data = await parser.get_item_data(lon=lon, lat=lat, item_name=item_name)
        if item_data:
            return item_data
        else:
            raise HTTPException(status_code=404, detail="Item data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stores/", response_model=List[Dict])
async def get_store(lon: float, lat: float) -> List[Dict]:
    parser = SberParser2()
    try:
        store_data = await parser.get_stores(lon=lon, lat=lat)
        print(store_data)
        if store_data:
            return store_data
        else:
            raise HTTPException(status_code=404, detail="Stores data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))