from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

def load_users():
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users

def save_user(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)

app = FastAPI()

class User(BaseModel):

    id: Annotated[str, Field(..., description='ID of the user', examples=['P001'])]
    first_name: Annotated[str, Field(..., description='First name of the user')]
    last_name: Annotated[str, Field(..., description='Last name of the user')]
    age: Annotated[int, Field(..., gt=18, lt=65, description='Age of the user')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the user')]

    @computed_field
    @property
    def full_name(self) -> str:
        return self.first_name + " " + self.last_name


@app.get("/")
def hello():
    return {'message':'Hello FastAPI'}

@app.post('/create')
def create_user(user: User):

    data = load_users()

    if user.id in data:
        raise HTTPException(status_code=400, detail='User already exists')

    # Convert pydantic object into python dict
    data[user.id] = user.model_dump(exclude={'id'})

    save_user(data)

    return JSONResponse(status_code=201, content={'message':'User created successfully'})

