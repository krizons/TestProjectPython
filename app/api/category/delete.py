from fastapi import APIRouter, Depends
from .model import *
from app.database import ApiDB
import aiofiles
from app.database import (
    ApiDB,
    category,
    document
)
router = APIRouter()


@router.delete("/",
               summary="Запрос на далениие категории",
               response_model=DeleteCategoryResponse,
               response_description="Ответ на запрос удаления категории")
async def delete_category(req: DeleteCategoryRequest = Depends()):  # ,
    # credentials: HTTPBasicCredentials = Depends(security)):
    #  get_current_username(credentials)
    list_id = [req.CategoryId]
    qu_id = [req.CategoryId]
    list_path = []
    while len(qu_id) != 0:
        qu = category.select().where(category.c.subid == qu_id[0])
        row = await ApiDB.fetch_all(qu)
        await ApiDB.execute(category.delete().where(category.c.id == qu_id[0]))
        qu_id.remove(qu_id[0])
        for el in row:
            qu_id.append(el.get("id"))
            list_id.append(el.get("id"))
    for id in list_id:
        qu = document.select().where(document.c.lincid == id)
        row = await ApiDB.fetch_all(qu)
        await ApiDB.execute(document.delete().where(document.c.lincid == id))
        for el in row:
            list_path.append(el.get("path"))
    for el in list_path:
        await aiofiles.os.remove(el)
    return DeleteCategoryResponse(status="Ok", result="")
