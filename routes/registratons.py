import stat
from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.registration import Registration, RegistrationCreate
from services.registration_service import registration_service
from services.user_service import user_service
from services.event_service import event_service
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=Registration, status_code=status.HTTP_201_CREATED)
async def create_registration(registration: RegistrationCreate):
    user = user_service.get_user(registration.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User is not active")
    event = event_service.get_event(registration.event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    if not event.is_open:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Event is not open")

# Users cannot register more than once for the same event
    existing_registration = next((reg for reg in registration_service.get_registrations(
    ) if reg.user_id == registration.user_id and reg.event_id == registration.event_id), None)
    if existing_registration:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User has already registered for this event")

    new_registration = registration_service.create_registration(registration)
    if new_registration is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create registration")
    return new_registration


@router.get("/", response_model=List[Registration])
async def read_registrations():
    return registration_service.get_registrations()


@router.get("/{registration_id}", response_model=Registration)
async def read_registration(registration_id: int):
    registration = registration_service.get_registration(registration_id)
    if registration is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Registration not found")
    return registration


@router.put("/{registration_id}/attended", response_model=Registration)
async def update_registration_attendance(registration_id: int, attended: bool):
    updated_registration = registration_service.update_registration(
        registration_id, attended)
    if updated_registration is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Registration not found")
    return updated_registration


@router.delete("/{registration_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_registration(registration_id: int):
    if not registration_service.delete_registration(registration_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Registration not found")
    return


@router.get("/event/{event_id}", response_model=List[Registration])
async def get_registrations_for_event(event_id: int):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return registration_service.get_registrations_by_event(event_id)


@router.get("/user/{user_id}", response_model=List[Registration])
async def get_registrations_by_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return registration_service.get_registrations_by_user(user_id)
