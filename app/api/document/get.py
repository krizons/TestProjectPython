from fastapi import APIRouter
from app.database import ApiDB
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/",
            summary="Запрос на получение файла",
            response_description="Файл")
async def get_document(file_id: int):  # , credentials: HTTPBasicCredentials = Depends(security)):
    # get_current_username(credentials)
    val = await ApiDB.GetDocument(file_id)
    return FileResponse(val)
