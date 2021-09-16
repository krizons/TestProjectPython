from fastapi import FastAPI

from dotenv import load_dotenv

import uvicorn
import os
from database import ApiDB
import api




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DEFINE_PATH: str = os.path.abspath(os.path.dirname(__file__)) + "\\files\\"
app = FastAPI()

app.include_router(
    api.router
)


@app.on_event("startup")
async def startup():
    await ApiDB.connect()


@app.on_event("shutdown")
async def shutdown():
    await ApiDB.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
# uvicorn ApiServer:app --reload
