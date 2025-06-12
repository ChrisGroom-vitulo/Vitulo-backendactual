
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def map_animals():
    return [{"lat": 54.0, "lon": -2.0, "tag": "UK123"}]
