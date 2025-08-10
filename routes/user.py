from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import func
from sqlmodel import Session, select
from config.sqlite import get_session
from models.user import User, UserCreate, UserRead

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    new_email = user.email.strip().lower()

    exists = session.exec(select(User).where(func.lower(User.email) == new_email)).first()
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    new_user = User(name=user.name, email=new_email, password=user.password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.put("/{id}", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def update_user(id: int, updated: UserCreate, session: Session = Depends(get_session)):
    db_user = session.get(User, id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )

    new_email = updated.email.strip().lower()
    duplicate = session.exec(
        select(User).where(func.lower(User.email) == new_email, User.id != id)
    ).first()
    if duplicate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    db_user.name = updated.name
    db_user.email = new_email
    db_user.password = updated.password

    session.add(db_user)
    session.commit()

    users = session.exec(select(User)).all()
    return users

@router.delete("/{id}", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def delete_user(id: int, session: Session = Depends(get_session)):
    db_user = session.get(User, id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )

    session.delete(db_user)
    session.commit()

    users = session.exec(select(User)).all()
    return users

