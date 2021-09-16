from fastapi import APIRouter
from . import category, document

router = APIRouter()

router.include_router(
    category.router,
    prefix="/category"
)

router.include_router(
    document.router,
    prefix="/document"
)
