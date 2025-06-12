
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Cattle(BaseModel):
    id: int
    tag_number: str
    breed: str
    purchase_price: float
    farm: str
    sex: Optional[str] = None
    dob: Optional[str] = None

db: List[Cattle] = []

@router.get("/cattle/", response_model=List[Cattle])
def get_all_cattle():
    return db

@router.post("/cattle/", response_model=Cattle)
def add_cattle(cow: Cattle):
    db.append(cow)
    return cow

@router.get("/cattle/{id}", response_model=Cattle)
def get_cow(id: int):
    return next(c for c in db if c.id == id)

@router.delete("/cattle/{id}")
def delete_cow(id: int):
    global db
    db = [c for c in db if c.id != id]
    return {"message": "Deleted"}
