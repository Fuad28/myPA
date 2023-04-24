from tortoise.models import Model
from tortoise import fields

class User(Model):
    """ Table for all users. """

    id = fields.IntField(pk = True)
    full_name = fields.CharField(max_length= 100)
    email = fields.CharField(max_length= 255, unique = True)
    password = fields.CharField(max_length= 100)
    is_active = fields.BooleanField(default= False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    # # It is useful to define the reverse relations manually so that type checking and auto completion work
    # events: fields.ReverseRelation["User"] #user should be replaced by the FK model.
