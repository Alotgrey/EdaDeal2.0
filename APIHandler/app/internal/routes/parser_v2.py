from fastapi import APIRouter, HTTPException

from APIHandler.app.pkg.sbermarket2_module.app.src.sber_parser2 import SberParser2
from APIHandler.app.pkg.sbermarket2_module.app.utils.constants import CHROME_PATH
from APIHandler.app.pkg.sbermarket2_module.app.utils.data_fetcher import DataFetcher


router = APIRouter(prefix="/api/v2/parser")


@router.post("/item/url/")
async def get_item_data(url: str, number_market: int) -> dict:
    with DataFetcher(CHROME_PATH) as fetcher:
        parser = SberParser2()
        try:
            item_data = await parser.get_item_data(url=url, number_market=number_market, prev_ver=True, fetcher=fetcher)
            if item_data:
                return item_data
            else:
                raise HTTPException(status_code=404, detail="Item data not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
