from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from database import (
    ApiDB,
    document
)
from depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.get("/",
            summary="Запрос на получение файла",
            response_description="Файл")
async def get_document(file_id: int, credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = document.select().where(document.c.id == file_id)
    row = await ApiDB.fetch_one(qu)
    return FileResponse(row.get("path"))
