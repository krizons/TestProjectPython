from pydantic import BaseModel
from typing import Optional
from fastapi import File, UploadFile


class CreateCategoryRequest(BaseModel):
    heading: str
    subtitle: str
    description: str
    subid: Optional[int] = 0

    class Config:
        title = "Запрос на создание категории или под категории"

        fields = dict(
            heading=dict(
                title="Заголовок"
            ),
            subtitle=dict(
                title="Подзаголовок"
            ),
            description=dict(
                title="Описание"
            ),
            subid=dict(
                title="Id заголовка или под заголовка"
            )
        )


class CreateCategoryResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Запрос на сложение A и B"
        fields = dict(
            A=dict(
                title="Первое слагаемое"
            ),
            B=dict(
                title="Второй слагаемое"
            )
        )


class EditCategoryRequest(BaseModel):
    id: int
    heading: Optional[str] = None
    subtitle: Optional[str] = None
    description: Optional[str] = None
    subid: Optional[int] = None

    class Config:
        title = "Запрос на изменение категории"
        fields = dict(
            id=dict(
                title="Id категории"
            ),
            heading=dict(
                title="Заголовок"
            ),
            subtitle=dict(
                title="Подзаголовок"
            ),
            description=dict(
                title="Описание"
            ),
            subid=dict(
                title="Id заголовка или под заголовка"
            )
        )


class EditCategoryResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Ответ на запрос изменения категории"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="описание события"
            )
        )


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


class AllCategoryRequest(BaseModel):
    CategoryId: Optional[int] = 0

    class Config:
        title = "Запрос на получение списка категорий или подкатегорий"
        fields = dict(
            subid=dict(
                title="Id категории или подкатегории"
            )
        )


class AllCategoryResponse(BaseModel):
    heading: str
    subtitle: str
    description: str
    id: int

    class Config:
        title = "Ответ на получение списка категорий или подкатегорий"
        fields = dict(
            heading=dict(
                title="Заголовок"
            ),
            id=dict(
                title="Id категории"
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
