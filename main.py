from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_users():
    with open("users.json", "r") as f:
        users = json.load(f)
    return users

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}

@app.get("/users")
def users ():
    users = load_users()
    return users

@app.get('/sort')
def sort_users(sort_by: str = Query(..., description='Sort by height, weight or bmi'), order: str = Query('asc', description='sort in asc or dsc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field. Select from {valid_fields}')

    if order not in ['asc', 'dsc']:
        raise HTTPException(status_code=400, detail='Invalid order. Select between asc and dsc')

    data = load_users()

    sort_order = True if order=='dsc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.get("/user/{id}")
def user (id: str = Path(..., description="User ID", example="P001")):
    users = load_users()
    if id in users:
        return users[id]
    raise HTTPException(status_code=404, detail="User not found")