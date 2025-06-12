
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def cts_status():
    return {"status": "CTS integration placeholder"}
