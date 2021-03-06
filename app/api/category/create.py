from fastapi import APIRouter, Depends, File, UploadFile
from .model import *
import sqlalchemy
from conf import settings
import  random
import  aiofiles
from database import (
    ApiDB,
    category
)
from depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.post("/",
             summary='Запрос на создание категории или подкатегории',
             response_model=CreateCategoryResponse,
             response_description="Результат запроса на создание категории или подкатегории")
async def create_category(req: CreateCategoryRequest = Depends(), image: UploadFile = File(...),
                          credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(category).where(
        category.c.heading == req.heading,
        category.c.subid == req.subid)
    image_path = settings.IMAGE_SAVE_PATH + str(random.randint(0, 1000000)) + "_" + image.filename
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
                                 "subid": req.subid,
                                 "image": image_path})
            async with aiofiles.open(image_path, 'wb') as image_file:
                binfile = await image.read()
                await image_file.write(binfile)
            return CreateCategoryResponse(status="OK", result="")

    return CreateCategoryResponse(status="Fault", result="")
