from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String

# Shared fields
class UserBase(SQLModel):
    name: str
    email: str = Field(sa_column=Column("email", String, unique=True, index=True))

# Table model
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str

# Request model for create/put
class UserCreate(UserBase):
    password: str

# Response model (hides password)
class UserRead(UserBase):
    id: int

