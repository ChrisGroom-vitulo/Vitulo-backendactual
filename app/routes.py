
from fastapi import APIRouter
from app.models import Cattle

router = APIRouter()

@router.get("/")
def get_cattle():
    return [{"tag_number": "UK123", "breed": "Angus"}]
