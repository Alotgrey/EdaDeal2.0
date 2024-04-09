from fastapi import APIRouter

from APIHandler.app.pkg.sbermarket_module.app.sber import ItemParser


router = APIRouter(prefix="/api/v1/parser")


@router.post("/item/url/")
def get_item_data(url: str) -> dict:
    return ItemParser.run_item(url)
