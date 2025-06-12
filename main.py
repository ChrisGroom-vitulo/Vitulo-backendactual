from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
cattle_db = []

# Pydantic model
class Cattle(BaseModel):
    id: int
    tag_number: str
    breed: str
    purchase_price: float
    farm: str
    sex: str
    dob: str

@app.post("/cattle/", response_model=Cattle)
def add_cattle(cow: Cattle):
    cattle_db.append(cow)
    return cow

@app.get("/cattle/", response_model=List[Cattle])
def get_all_cattle():
    return cattle_db

