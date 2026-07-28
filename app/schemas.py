from pydantic import BaseModel, EmailStr
from typing import Dict, Any


class SurveySubmission(BaseModel):
    responses: Dict[str, Any]


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    organization: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    organization: str
    role: str

    class Config:
        from_attributes = True