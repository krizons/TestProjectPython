from fastapi import APIRouter, Depends
from .model import *
from app.database import ApiDB
router = APIRouter()


@router.get("/",
            summary="Запрос на получение всех категорий или подкатегорий выбраной категории",
            response_model=list,
            response_description="Результат запроса на получение всех категорий или подкатегорий выбраной категории")
async def all_category(req: AllCategoryRequest = Depends()):#, credentials: HTTPBasicCredentials = Depends(security)):
   # get_current_username(credentials)
    val = await ApiDB.GetAllCategory(req.CategoryId)
    data_response = []
    for el in val:
        data_response.append(
            AllCategoryResponse(heading=el.get("heading"), id=el.get("id"), subtitle=el.get("subtitle"),
                                description=el.get("description")))
    return data_response
