from fastapi import APIRouter, Depends
from .model import *
import sqlalchemy
from app.database import (
    ApiDB,
    category
)
from app.depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.post("/",
             summary='Запрос на создание категории или подкатегории',
             response_model=CreateCategoryResponse,
             response_description="Результат запроса на создание категории или подкатегории")
async def create_category(req: CreateCategoryRequest = Depends(),
                          credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(category).where(
        category.c.heading == req.heading,
        category.c.subid == req.subid)
    row = await ApiDB.fetch_one(qu)
    if row[0] == 0:
        qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(category).where(
            category.c.id == req.subid)
        row = await ApiDB.fetch_one(qu)
        if row[0] > 0 or req.subid == 0:
            await ApiDB.execute(category.insert(),
                                {"heading": req.heading,
                                 "subtitle": req.subtitle,
                                 "description": req.description,
                                 "subid": req.subid})
            return CreateCategoryResponse(status="OK", result="")

    return CreateCategoryResponse(status="Fault", result="")
