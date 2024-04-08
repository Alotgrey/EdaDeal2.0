from fastapi import APIRouter

from APIHandler.app.pkg.sbermarket_module.app.sber import itemParser


router = APIRouter(prefix="/api/v1/parser")


@router.post("/item/url/")
def get_item_data(url: str) -> dict:
    parser = itemParser()
    item_data = parser.run_item(url)[0]

    return {"price": float(item_data["price"])}
