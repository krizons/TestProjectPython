from fastapi import APIRouter, Depends
from .model import *
from app.database import (
    ApiDB,
    document,
)
from app.depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.get("/",
            summary="Запрос на получение всех файлов в выбраной категории или подкатегорий",
            response_model=list,
            response_description="Результат запроса на получение всех файлов в выбраной категории или подкатегорий")
async def all_document(req: AllDocumentRequest = Depends(),
                       credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    data_response = []
    qu = document.select().where(document.c.lincid == req.CategoryId)
    row = await ApiDB.fetch_all(qu)
    for el in row:
        data_response.append(
            AllDocumentResponse(name=el.get("name"), url="/get/document?file_id={0}".format(el.get("id"))))
    return data_response

