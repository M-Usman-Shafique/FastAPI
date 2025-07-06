from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Pydantic class
class User(BaseModel):
    name: Annotated[
        str,
        Field(
        min_length=3,
        max_length=25,
        title="Name of the user",
        description="Give the name of the user between 3 to 25 chars"),
        ]
    email: EmailStr
    url: AnyUrl
    age: int = Field(gt=18, lt=60, strict=True) # Type coercion disabled
    married: Optional[bool] = None
    skills: List[str] = Field(max_length=5)
    address: Dict[str, str]


# Raw data
user_dict = {
    "name": "Ali",
    "email": "ali@test.com",
    "url": "https://linkendin.com",
    "age": 30,
    "address": {"city": "Lahore", "country": "Pakistan"},
    "skills": ["Java", "Python", "Ruby"]
    }

# Pydantic object
user1 = User(**user_dict)

def show_user(user: User):
   print(user.name)
   print(user.email)
   print(user.age)
   print(user.address['city'])
   for skill in user.skills:
        print(skill)

# Pass pydantic obj to function
show_user(user1)