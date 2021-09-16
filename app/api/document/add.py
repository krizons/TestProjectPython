from fastapi import APIRouter,Depends
from .model import *
import sqlalchemy
import aiofiles
import os
from app.database import (
    ApiDB,
    category,
    document
)
from app.depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)


router = APIRouter()


@router.put("/",
            summary="Запрос на добавление документа в категорию или подкатегорию",
            response_model=AddDocumentResponse,
            response_description="Запрос на добавление документа в категорию или подкатегорию")
async def add_document(CategoryId: int, Document: UploadFile = File(...),
                       credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    new_path = os.environ["FILE_SAVE_PATH"] + str(
        CategoryId) + "_" + Document.filename
    try:
        qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(category).where(
            category.c.id == CategoryId)
        row = await ApiDB.fetch_one(qu)
        if row[0] != 0:
            qu = document.insert()
            await ApiDB.execute(qu, {"lincid": CategoryId,
                                     "name": Document.filename,
                                     "path": new_path})
            async with aiofiles.open(new_path, 'wb') as out_file:
                binfile = await Document.read()
                await out_file.write(binfile)
                return AddDocumentResponse(status="OK", result="")
    except:
        pass
    return AddDocumentResponse(status="Fault", result="")
