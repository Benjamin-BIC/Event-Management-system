from pydantic import BaseModel
from datetime import date


class Eventbase(BaseModel):
    title: str
    location: str
    date: date


class Event(Eventbase):
    id: int
    is_open: bool = False


class EventCreate(Event):
    pass
