from pydantic import BaseModel, EmailStr
class User(BaseModel):
    name: str
    email:EmailStr
    age: int
    gender: str = "Male"

user_dict = {
    "name": "Ali",
    "email": "ali@test.com",
    "age": 30,
    }

user1 = User(**user_dict)

temp1 = user1.model_dump_json() # all fields
temp2 = user1.model_dump_json(include={"name", "email"})
temp3 = user1.model_dump_json(exclude={"name", "email"})
print(temp1)
print(temp2)
print(temp3)
print(type(temp1))