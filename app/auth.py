
from fastapi import APIRouter, HTTPException
from app.schemas import LoginSchema, TokenSchema

router = APIRouter()

@router.post("/login", response_model=TokenSchema)
def login(payload: LoginSchema):
    if payload.username == "admin" and payload.password == "password":
        return {"access_token": "admin-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
