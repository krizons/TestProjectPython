from pydantic import BaseModel
from typing import Optional
from fastapi import File, UploadFile


class AddDocumentRequest(BaseModel):
    Document: UploadFile = File(...)
    CategoryId: int = 0

    class Config:
        title = "Запрос на добавление документа"
        fields = dict(
            Document=dict(
                title="Документ"
            ),
            CategoryId=dict(
                title="Id категории или подкатегории"
            )
        )


class AddDocumentResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Ответ на запрос добавления файла в категорию"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="описание события"
            )
        )


class DeleteDocumentRequest(BaseModel):
    Name: str
    CategoryId: int

    class Config:
        title = "Запрос на удаление файла"
        fields = dict(
            Name=dict(
                title="Имя файла"
            ),
            CategoryId=dict(
                title="Идентификатор категории можно получить используя /all/category"
            )
        )


class DeleteDocumentResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Ответ на запрос удаления файла"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="описание события"
            )
        )


class AllDocumentRequest(BaseModel):
    CategoryId: int = 0

    class Config:
        title = "Запрос на получение списка файлов в категории или подкатегории"
        fields = dict(
            CategoryId=dict(
                title="Id категории"
            ),

        )


class AllDocumentResponse(BaseModel):
    name: str
    url: str

    class Config:
        title = "Список файлов в данной категории"
        fields = dict(
            name=dict(
                title="Имя файла"
            ),
            url=dict(
                title="Ссылка на скачивание"
            )
        )
