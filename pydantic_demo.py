from pydantic import BaseModel
class Address(BaseModel):
    city: str
    state: str
    pin: int
class User(BaseModel):
    name: str
    age: int
    address: Address

address_dict = {
    "city": "Lahore",
    "state": "Punjab",
    "pin": 54000
}

address1 = Address(**address_dict)

user_dict = {
    "name": "Ali",
    "age": 30,
    "address": address1
    }

user1 = User(**user_dict)

def show_user(user: User):
   print(user.name)
   print(user.age)
   print(user.address.city)

show_user(user1)