from fastapi import APIRouter,Depends
from .model import *
from app.database import ApiDB

router = APIRouter()


@router.post("/",
             summary='Запрос на создание категории или подкатегории',
             response_model=CreateCategoryResponse,
             response_description="Результат запроса на создание категории или подкатегории")
async def create_category(req: CreateCategoryRequest = Depends()):#,
                          #credentials: HTTPBasicCredentials = Depends(security)):
    #get_current_username(credentials)
    val = await ApiDB.CreateCategory(req.heading,
                                     req.subtitle,
                                     req.description,
                                     req.subid)
    if val is True:
        return CreateCategoryResponse(status="OK", result="")
    else:
        return CreateCategoryResponse(status="Fault", result="")
