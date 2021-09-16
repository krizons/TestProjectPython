from fastapi import APIRouter, Depends
from .model import *
import aiofiles
from app.database import ApiDB

router = APIRouter()


@router.delete("/",
               summary="Запрос на удаление документа из категории или подкатегории",
               response_model=DeleteDocumentResponse,
               response_description="Результат запроса на удаление документа из категории или подкатегории")
async def delete_document(req: DeleteDocumentRequest = Depends()):
    val = await ApiDB.DeleteDocument(req.Name, req.CategoryId)
    if val is not None:
        await aiofiles.os.remove(val.get("path"))
        return DeleteDocumentResponse(status="OK", result="")
    return DeleteDocumentResponse(status="Fault", result="")
