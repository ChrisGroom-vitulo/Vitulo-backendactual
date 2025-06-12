
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_payments():
    return [{"month": "May", "total": 5000}]
