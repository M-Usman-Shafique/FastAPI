from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

# Pydantic class
class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    married: Optional[bool] = None
    skills: List[str]
    address: Dict[str, str]

    @model_validator(mode="after")
    def validate_AI_skill(cls, model):
        if model.age > 30 and "AI" not in model.skills:
            raise ValueError("Users older than 30 must have AI skill")
        return model



# Raw data
user_dict = {
    "name": "ali",
    "email": "ali@test.com",
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