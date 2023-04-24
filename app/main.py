from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core import settings

app = FastAPI(
    title= settings.TITLE,
)

register_tortoise(
    app,
    db_url= settings.DATABASE_URL, 
    modules= {"models": ["app.models"]}, 
    generate_schemas=True, 
    add_exception_handlers= True)