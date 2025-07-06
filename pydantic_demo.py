from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

# Pydantic class
class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    married: Optional[bool] = None
    skills: List[str]
    address: Dict[str, str]

    @computed_field
    @property
    def full_name(self) -> str:
        return self.first_name + " " + self.last_name



# Raw data
user_dict = {
    "first_name": "Ali",
    "last_name": "Khan",
    "email": "ali@test.com",
    "age": 30,
    "address": {"city": "Lahore", "country": "Pakistan"},
    "skills": ["Java", "Python", "Ruby"]
    }

# Pydantic object
user1 = User(**user_dict)

def show_user(user: User):
   print(user.full_name)
   print(user.email)
   print(user.age)
   print(user.address['city'])
   for skill in user.skills:
        print(skill)

# Pass pydantic obj to function
show_user(user1)