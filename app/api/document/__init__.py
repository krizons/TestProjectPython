from fastapi import APIRouter
from . import (
    all,
    add,
    delete,
    get

)

router = APIRouter()

router.include_router(
    all.router,
    prefix="/all"
)

router.include_router(
    add.router,
    prefix="/add"
)

router.include_router(
    delete.router,
    prefix="/delete"
)

router.include_router(
    get.router,
    prefix="/get"
)
