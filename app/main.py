from fastapi import FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
import secrets
import uvicorn
import os
from database import ApiDB
import api

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(credentials.username, os.environ["LOGIN"])
    correct_password = secrets.compare_digest(credentials.password, os.environ["PASS"])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DEFINE_PATH: str = os.path.abspath(os.path.dirname(__file__)) + "\\files\\"
app = FastAPI()

app.include_router(
    api.router
)


@app.on_event("startup")
async def startup():
    pass
    await ApiDB.ConnectBd()


@app.on_event("shutdown")
async def shutdown():
    await ApiDB.Close()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
# uvicorn ApiServer:app --reload
