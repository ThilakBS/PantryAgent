from fastapi import FastAPI
from routers.pantry import router as pantry_router

app = FastAPI()

app.include_router(pantry_router)
