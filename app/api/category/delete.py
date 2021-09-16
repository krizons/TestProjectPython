from fastapi import APIRouter, Depends
from .model import *
from app.database import ApiDB
import aiofiles

router = APIRouter()


@router.delete("/",
               summary="Запрос на далениие категории",
               response_model=DeleteCategoryResponse,
               response_description="Ответ на запрос удаления категории")
async def delete_category(req: DeleteCategoryRequest = Depends()):  # ,
    # credentials: HTTPBasicCredentials = Depends(security)):
    #  get_current_username(credentials)
    val = await ApiDB.DeleteCategor(req.CategoryId)
    for el in val:
        await aiofiles.os.remove(el)
    return DeleteCategoryResponse(status="Ok", result="")
