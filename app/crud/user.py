from app.core.exceptions import BadRequest
from app.schemas import UserSchema, UserInSchema
from app.models import User

async def create_user(user: UserInSchema):
    user = await User.filter(email = user.email).first()

    if user:
        raise BadRequest("User exists already")
    
    user_dict = user.dict()
    
