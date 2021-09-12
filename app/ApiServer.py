from fastapi import FastAPI, Depends, File, UploadFile, Query
from fastapi.responses import FileResponse
from app.Model import *
from dotenv import load_dotenv

from app.Bd import TestApiBd
import uvicorn
import os
import aiofiles
import aiofiles.os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DEFINE_PATH: str = os.path.abspath(os.path.dirname(__file__)) + "\\files\\"
app = FastAPI()

ApiBd: TestApiBd = TestApiBd(os.environ["DATABASE_URL"])


@app.on_event("startup")
async def startup():
    pass
    await ApiBd.ConnectBd()


@app.on_event("shutdown")
async def shutdown():
    await ApiBd.Close()


@app.post("/create/category",
          summary="Запрос на создание категории или подкатегории",
          response_model=CreateCategoryResponse,
          response_description="Результат запроса на создание категории или подкатегории")
async def create_category(req: CreateCategoryRequest = Depends()):
    val = await ApiBd.CreateCategory(req.heading,
                                     req.subtitle,
                                     req.description,
                                     req.subid)
    if val is True:
        return CreateCategoryResponse(status="OK", result="")
    else:
        return CreateCategoryResponse(status="Fault", result="")


@app.post("/edit/category",

          summary="Запрос на изменение категории или подкатегории",
          response_model=EditCategoryResponse,
          response_description="Результат запроса на изменение категории или подкатегории")
async def edit_category(req: EditCategoryRequest = Depends()):
    if await ApiBd.EditCategory(req.id, req.heading, req.subtitle, req.description, req.subid):
        return EditCategoryResponse(status="OK", result="")
    return EditCategoryResponse(status="Fault", result="")


@app.put("/add/document",
         summary="Запрос на добавление документа в категорию или подкатегорию",
         response_model=AddDocumentResponse,
         response_description="Запрос на добавление документа в категорию или подкатегорию")
async def add_document(CategoryId: int, Document: UploadFile = File(...)):
    new_path = DEFINE_PATH + "_" + str(CategoryId) + "_" + Document.filename
    if await ApiBd.AddDocument(CategoryId, Document.filename, new_path):
        async with aiofiles.open(new_path, 'wb') as out_file:
            binfile = await Document.read()
            await out_file.write(binfile)
        return AddDocumentResponse(status="OK", result="")
    return AddDocumentResponse(status="Fault", result="")


@app.delete("/delete/document",
            summary="Запрос на удаление документа из категории или подкатегории",
            response_model=DeleteDocumentResponse,
            response_description="Результат запроса на удаление документа из категории или подкатегории")
async def delete_document(req: DeleteDocumentRequest = Depends()):
    val = await ApiBd.DeleteDocument(req.Name, req.CategoryId)
    if val is not None:
        await aiofiles.os.remove(val.get("path"))
        return DeleteDocumentResponse(status="OK", result="")
    return DeleteDocumentResponse(status="Fault", result="")


@app.get("/all/category",
         summary="Запрос на получение всех категорий или подкатегорий выбраной категории",
         response_model=list,
         response_description="Результат запроса на получение всех категорий или подкатегорий выбраной категории")
async def all_category(req: AllCategoryRequest = Depends()):
    val = await ApiBd.GetAllCategory(req.CategoryId)
    data_response = []
    for el in val:
        data_response.append(
            AllCategoryResponse(heading=el.get("heading"), id=el.get("id"), subtitle=el.get("subtitle"),
                                description=el.get("description")))
    return data_response


@app.get("/all/document",
         summary="Запрос на получение всех файлов в выбраной категории или подкатегорий",
         response_model=list,
         response_description="Результат запроса на получение всех файлов в выбраной категории или подкатегорий")
async def all_document(req: AllDocumentRequest = Depends()):
    data_response = []
    val = await ApiBd.GetAllDocument(req.CategoryId)
    for el in val:
        data_response.append(
            AllDocumentResponse(name=el.get("name"), url="/get/document?file_id={0}".format(el.get("id"))))
    return data_response


@app.get("/get/document",
         summary="Запрос на получение файла",
         response_description="Файл")
async def get_document(file_id: int):
    val = await ApiBd.GetDocument(file_id)
    # response = FileResponse(val)
    return FileResponse(val)


@app.delete("/delete/category",
            summary="Запрос на далениие категории",
            response_model=DeleteCategoryResponse,
            response_description="Ответ на запрос удаления категории")
async def delete_category(req: DeleteCategoryRequest= Depends()):
    # val = await ApiBd.GetDocument(file_id)
    # response = FileResponse(val)
    val=await ApiBd.DeleteCategor(req.CategoryId)
    for el in val:
        await aiofiles.os.remove(el)
    return DeleteCategoryResponse(status="Ok", result="")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
# uvicorn ApiServer:app --reload
