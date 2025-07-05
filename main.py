from fastapi import FastAPI, Path, HTTPException
import json

def loadUsers():
    with open("users.json", "r") as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}

@app.get("/users")
def users ():
    users = loadUsers()
    return users

@app.get("/user/{id}")
def user (id: str = Path(..., description="User ID", example="P001")):
    users = loadUsers()
    if id in users:
        return users[id]
    raise HTTPException(status_code=404, detail="User not found")