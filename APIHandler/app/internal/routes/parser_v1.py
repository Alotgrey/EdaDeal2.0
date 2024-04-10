from fastapi import APIRouter, HTTPException

from APIHandler.app.pkg.sbermarket_module.app.sber import ItemParser


router = APIRouter(prefix="/api/v1/parser")


@router.post("/item/url/")
def get_item_data(url: str) -> dict:
    try:
        item_data = ItemParser.run_item(url)
        if item_data:
            return item_data
        else:
            raise HTTPException(status_code=404, detail="Item data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
