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
        title = "Результат на запрос создание категории или под категории"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="Сообщение"
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


class DeleteCategoryRequest(BaseModel):
    CategoryId: int

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


class DeleteCategoryResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Ответ на запрос добавления файла в категорию"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="Сообщение"
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
            subtitle=dict(
                title="Подзаголовок"
            ),
            description=dict(
                title="Описание"
            ),
            id=dict(
                title="Id категории"
            )
        )
