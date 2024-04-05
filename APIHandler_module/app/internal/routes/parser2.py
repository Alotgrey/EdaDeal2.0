from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v2/parser'
)

@router.post('/item/url/')
def get_item_data(url: str) -> dict:
    ...
    return {}