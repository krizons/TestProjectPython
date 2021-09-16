from fastapi import APIRouter, Depends
from .model import *
from app.database import ApiDB

router = APIRouter()


@router.post("/",
             summary="Запрос на изменение категории или подкатегории",
             response_model=EditCategoryResponse,
             response_description="Результат запроса на изменение категории или подкатегории")
async def edit_category(
        req: EditCategoryRequest = Depends()):  # , credentials: HTTPBasicCredentials = Depends(security)):
    # get_current_username(credentials)
    if await ApiDB.EditCategory(req.id, req.heading, req.subtitle, req.description, req.subid):
        return EditCategoryResponse(status="OK", result="")
    return EditCategoryResponse(status="Fault", result="")
