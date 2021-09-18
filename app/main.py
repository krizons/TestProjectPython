from fastapi import FastAPI
from database import ApiDB
import api
from  conf import settings
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

# if __name__ == "__main__":
#  uvicorn.run(app, host="localhost", port=8000)
# uvicorn ApiServer:app --reload
