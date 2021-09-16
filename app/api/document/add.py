from fastapi import APIRouter
from .model import *
from app.database import ApiDB
import aiofiles
import  os
router = APIRouter()


@router.put("/",
            summary="Запрос на добавление документа в категорию или подкатегорию",
            response_model=AddDocumentResponse,
            response_description="Запрос на добавление документа в категорию или подкатегорию")
async def add_document(CategoryId: int, Document: UploadFile = File(...)):  # ,
    # credentials: HTTPBasicCredentials = Depends(security)):
    # get_current_username(credentials)
    new_path = os.environ["FILE_SAVE_PATH"]  # DEFINE_PATH + "_" + str(CategoryId) + "_" + Document.filename
    if await ApiDB.AddDocument(CategoryId, Document.filename, new_path):
        async with aiofiles.open(new_path, 'wb') as out_file:
            binfile = await Document.read()
            await out_file.write(binfile)
        return AddDocumentResponse(status="OK", result="")
    return AddDocumentResponse(status="Fault", result="")
