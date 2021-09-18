from fastapi import APIRouter, Depends
from .model import *
import aiofiles.os
import os.path
from database import (
    ApiDB,
    document,
)
from depends import (
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
    qu = document.delete().returning(document.c.path).where(document.c.id == req.document_id)
    row = await ApiDB.fetch_one(qu)
    if row is not None:
        if os.path.isfile(row.get("path")):
            await aiofiles.os.remove(row.get("path"))
            return DeleteDocumentResponse(status="OK", result="")

    return DeleteDocumentResponse(status="Fault", result="")
