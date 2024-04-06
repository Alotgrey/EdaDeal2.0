from fastapi import APIRouter


router = APIRouter(prefix="/api/v2/parser")


@router.post("/item/url/")
def get_item_data(url: str) -> dict:
    # TODO: Доделать V2
    return {'error': "NotImplementedError"}
    # parser = itemParser()
    # item_data = parser.run_item(url)[0]

    # return {"price": float(item_data["price"])}
