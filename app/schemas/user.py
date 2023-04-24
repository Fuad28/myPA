from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.user import User

UserSchema = pydantic_model_creator(User, exclude= ["password"])
UserInSchema = pydantic_model_creator(User, exclude_readonly= True)