from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
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

class UserUpdate(BaseModel):
    first_name: Annotated[Optional[str], Field(default=None)]
    last_name: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]


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

@app.put('/edit/{id}')
def update_user(id: str, user_update: UserUpdate):

    data = load_users()

    if id not in data:
        raise HTTPException(status_code=404, detail='User not found')

    # Extract user to update
    existing_user = data[id]

    # Convert pydantic obj into python dict and allow only the set (edited) fields
    updated_user = user_update.model_dump(exclude_unset=True)

    for key, value in updated_user.items():
        existing_user[key] = value

    existing_user['id'] = id

    # Convert the python dict again into pydantic obj to let the fields ("full_name") recalculated
    user_pydandic_obj = User(**existing_user)

    # Convert pydantic obj back into python dict and exclude "id"
    existing_user = user_pydandic_obj.model_dump(exclude={'id'})

    # Add updated dict into users data
    data[id] = existing_user

    save_user(data)

    return JSONResponse(status_code=200, content={'message':'User updated'})

@app.delete('/delete/{id}')
def delete_user(id: str):

    data = load_users()

    if id not in data:
        raise HTTPException(status_code=404, detail='User not found')

    del data[id]

    save_user(data)

    return JSONResponse(status_code=200, content={'message':'User deleted'})