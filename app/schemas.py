
from pydantic import BaseModel

class LoginSchema(BaseModel):
    username: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class UploadSchema(BaseModel):
    file_name: str
    status: str
