from fastapi import FastAPI
from routes.predict import router as predict_router

app = FastAPI()

@app.get("/")
def root():
    return {'message':'Hello FastAPI'}

app.include_router(predict_router, prefix="/api", tags=["Prediction"])