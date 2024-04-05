from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v2/parser'
)

@router.post('/items/get_price/')
def get_price(url: str) -> float:
    ...