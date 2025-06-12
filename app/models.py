
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Cattle(BaseModel):
    id: Optional[int]
    tag_number: str
    breed: str
    purchase_price: float
    farm: str
    sex: str
    dob: date
    current_value: Optional[float]

class KillRecord(BaseModel):
    id: Optional[int]
    tag_number: str
    slaughter_date: date
    carcass_weight: float
    grade: str
    value: float

class User(BaseModel):
    id: Optional[int]
    username: str
    password: str
    role: str  # 'admin', 'dairy', 'beef'
