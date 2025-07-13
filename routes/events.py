from logging import raiseExceptions
from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.event import Event, EventCreate
from services.event_service import event_service

router = APIRouter()


@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(event: EventCreate):
    return event_service.create_event(event)


@router.get("/", response_model=List[Event])
async def read_events():
    return event_service.get_events


@router.get("/{event_id}", response_model=Event)
async def read_event(event_id: int):
    event = event_service.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.put("/{event_id}", response_model=Event)
async def update_event(event_id: int, event: EventCreate):
    updated_event = event_service.update_event(event_id, event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: int):
    if not event_service.delete_event(event_id):
        raise HTTPException(status_code=404, detail="Event not found")
    return
