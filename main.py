from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {'data': 'Hello FastAPI'}

@app.get("/blog")
def blog(limit = 10, skip = 10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs'}
    else:
        return {'data': f'{limit} blogs'}

@app.get("/blog/{id}")
def blog(id: int):
    return {'data': id}