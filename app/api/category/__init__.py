from fastapi import APIRouter
from . import (
    all,
    create,
    delete,
    edit

)

router = APIRouter()

router.include_router(
    all.router,
    prefix="/all"
)

router.include_router(
    create.router,
    prefix="/create"
)

router.include_router(
    delete.router,
    prefix="/delete"
)

router.include_router(
    edit.router,
    prefix="/edit"
)
