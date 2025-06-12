
from fastapi import APIRouter
from app.models import KillRecord

router = APIRouter()

@router.get("/")
def get_kill_data():
    return [{"tag_number": "UK123", "value": 820.5}]
