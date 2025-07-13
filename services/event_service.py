import re
from typing import List, Optional
from schemas.event import EventCreate, Event
from datetime import date


class EventService:
    def __init__(self):
        self.events_db = []
        self.next_id = 1

    def create_event(self, event: EventCreate) -> Event:
        db_event = Event(id=self.next_id, **event.model_dump())
        self.events_db.append(db_event)
        self.next_id += 1
        return db_event

    def get_event(self, event_id: int) -> Optional[Event]:
        for event in self.events_db:
            if event.id == event_id:
                return event
        return None

    def get_events(self) -> List[Event]:
        return self.events_db

    def update_event(self, event_id: int, event: EventCreate) -> Optional[Event]:
        for i, event in enumerate(self.events_db):
            if event.id == event_id:
                updated_event = event.model_copy(update=event.model_dump())
                self.events_db[i] = updated_event
                return updated_event
            return None

    def delete_event(self, event_id: int) -> bool:
        initial_len = len(self.events_db)
        self.events_db = [
            event for event in self.events_db if event.id != event_id]
        return len(self.events_db) != initial_len


event_service = EventService()
