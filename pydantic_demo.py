from pydantic import BaseModel

# Pydantic class
class User(BaseModel):
    name: str
    age: int

# Raw data
user_dict = {"name": "Ali", "age": 30}

# Pydantic object
user1 = User(**user_dict)

def show_user(user: User):
   print(user.name)
   print(user.age)

# Pass pydantic obj to function
show_user(user1)