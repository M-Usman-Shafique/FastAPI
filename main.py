from fastapi import FastAPI
from typing import Optional
import schemas

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


@app.post("/blog")
def create_blog(blog: schemas.Blog):
    return {'data': {
        'title': blog.title,
        'description': blog.description,
    }}