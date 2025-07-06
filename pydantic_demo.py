from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Optional

# Pydantic class
class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    married: Optional[bool] = None
    skills: List[str]
    address: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_TLD = ["com", "org", "net"]
        domain_name = value.split(".")[-1]

        if domain_name not in valid_TLD:
            raise ValueError("Invalid email.")

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.title()


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