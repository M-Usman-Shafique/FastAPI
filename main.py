from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.user import router as user_router
from config.sqlite import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="FastAPI",
    description="A server application.",
    openapi_tags=[
                {"name": "Users", "description": "User Management"},
    ],
    version="v1",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {'message':'Hello FastAPI'}

app.include_router(user_router, prefix="/api", dependencies=[])
