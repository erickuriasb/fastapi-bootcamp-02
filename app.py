from fastapi import FastAPI, APIRouter

import models
from config.db import engine
from routes import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])


app.include_router(api_router, prefix='/api')

@app.get('/')
def root():
    return {
        "Hello": "World"
    }