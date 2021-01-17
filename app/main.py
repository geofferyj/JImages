from fastapi import FastAPI
from routes.images_route import router as ImagesRouter

app = FastAPI()

app.include_router(ImagesRouter, tags=["Images"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}