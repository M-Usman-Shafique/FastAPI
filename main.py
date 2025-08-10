from fastapi import FastAPI, Depends
from routes.user import router as user_router
from services.require_user import require_user

app = FastAPI(
    title="FastAPI",
    description="A server application.",
    openapi_tags=[
                {"name": "Users", "description": "User Management"},
    ],
    version="v1",
)

@app.get("/")
def root():
    return {'message':'Hello FastAPI'}

app.include_router(user_router, prefix="/api", dependencies=[Depends(require_user)])
