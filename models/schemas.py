from pydantic import BaseModel
from typing import Optional


class AuthDetails(BaseModel):
    username: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    is_admin: bool = False
    is_active: bool = True
    is_student: bool = False

def authDetailsSerial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "is_admin": user["is_admin"],
        "is_active": user["is_active"],
        "is_student": user["is_student"]
    }

def authsDetailsSerial(users) -> list:
    return [authDetailsSerial(user) for user in users]