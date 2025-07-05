from fastapi import FastAPI
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
def user (id: str):
    users = loadUsers()
    if id in users:
        return users[id]
    return {"error": "User not found"}