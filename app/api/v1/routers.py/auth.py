from fastapi import APIRouter

from app.schemas import UserSchema, UserInSchema
from app.models import User
from app.crud import create_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

"""
user registration
account activation
user login
"""

@router.post("/register/")
async def register_user(data: UserInSchema):
    user = create_user(data)
    

