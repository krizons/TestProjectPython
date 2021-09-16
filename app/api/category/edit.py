from fastapi import APIRouter, Depends
from .model import *
from app.database import (
    ApiDB,
    category
)

router = APIRouter()


@router.post("/",
             summary="Запрос на изменение категории или подкатегории",
             response_model=EditCategoryResponse,
             response_description="Результат запроса на изменение категории или подкатегории")
async def edit_category(
        req: EditCategoryRequest = Depends()):  # , credentials: HTTPBasicCredentials = Depends(security)):
    # get_current_username(credentials)
    param = {}
    if req.heading is not None:
        param["heading"] = req.heading
    if req.subtitle is not None:
        param["subtitle"] = req.subtitle
    if req.description is not None:
        param["description"] = req.description
    if req.subid is not None:
        param["subid"] = req.subid
    if len(param) > 0:
        qu = category.update().where(category.c.id == req.id).values(param)
        try:
            await ApiDB.execute(qu)
            return EditCategoryResponse(status="OK", result="")
        except:
            pass
    return EditCategoryResponse(status="Fault", result="")
