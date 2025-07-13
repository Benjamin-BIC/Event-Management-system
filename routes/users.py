from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.user import User, UserCreate
from services.user_service import user_service
from services.registration_service import registration_service

router = APIRouter()


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.get("/", response_model=List[User])
async def read_users():
    return user_service.get_users()


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    updated_user = user_service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return


@router.get("/attended-events/", response_model=List[User])
async def get_users_attended_events():
    attended_user_ids = set()
    for registration in registration_service.get_registrations():
        if registration.attended:
            attended_user_ids.add(registration.user_id)
    attended_users = []
    for user_id in attended_user_ids:
        user = user_service.get_user(user_id)
        if user:
            attended_users.append(user)
    return attended_users
