from fastapi import APIRouter, Depends
from .model import *
import aiofiles.os
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


@router.delete("/",
               summary="Запрос на удаление документа из категории или подкатегории",
               response_model=DeleteDocumentResponse,
               response_description="Результат запроса на удаление документа из категории или подкатегории")
async def delete_document(req: DeleteDocumentRequest = Depends(),
                          credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = not document.delete().returning(document.c.path).where(document.c.name == req.Name,
                                                                document.c.lincid == req.CategoryId)
    row = await ApiDB.fetch_one(qu)
    if row is not None:
        await aiofiles.os.remove(row.get("path"))
        return DeleteDocumentResponse(status="OK", result="")
    return DeleteDocumentResponse(status="Fault", result="")
