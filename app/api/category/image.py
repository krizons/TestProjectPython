from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
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


@router.get("/",
            summary="Запрос на получение изображения категории",
            response_description="Изображение")
async def get_document(id: int, credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = category.select().where(category.c.id == id)
    row = await ApiDB.fetch_one(qu)
    return FileResponse(row.get("image"))