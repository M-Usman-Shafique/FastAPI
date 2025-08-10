from fastapi import APIRouter, HTTPException, status
from data.user import USERS
from models.user import User

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("", response_model=list[User], status_code=status.HTTP_200_OK)
def get_users():
    return USERS

@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    new_email = user.email.strip().lower()
    if any(u.email.strip().lower() == new_email for u in USERS):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )
    USERS.append(user)
    return user

@router.put("/{id}", response_model=list[User], status_code=status.HTTP_200_OK)
def update_user(id: int, updated_user: User):
    for index, existing_user in enumerate(USERS):
        if existing_user.id == id:
            new_email = updated_user.email.strip().lower()
            if any(
                u.email.strip().lower() == new_email and u.id != id
                for u in USERS
            ):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email already exists",
                )
            USERS[index] = updated_user
            return USERS
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {id} not found",
    )

@router.delete("/{id}", response_model=list[User], status_code=status.HTTP_200_OK)
def delete_user(id: int):
    for index, existing_user in enumerate(USERS):
        if existing_user.id == id:
            USERS.pop(index)
            return USERS
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {id} not found",
    )
