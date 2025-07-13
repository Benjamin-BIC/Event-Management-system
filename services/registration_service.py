from typing import List, Optional
from schemas.registration import Registration, RegistrationCreate
from services.event_service import event_service
from services.user_service import user_service
from datetime import datetime


class RegistrationService:
    def __init__(self):
        self.registrations_db = []
        self.next_id = 1

    def create_registration(self, registration: RegistrationCreate) -> Optional[Registration]:
        user = user_service.get_user(registration.user_id)
        if not user or not user.is_active:
            return None  # User not found or not active
        event = event_service.get_event(registration.event_id)
        if not event or not event.is_open:
            return None  # Event not found or not open for registration

        # prevent duplicate registration for the same user and event
        for reg in self.registrations_db:
            if reg.user_id == registration.user_id and reg.event_id == registration.event_id:
                return None  # Already registered

        db_registration = Registration(
            id=self.next_id, registration_date=datetime.now(), **registration.model_dump())
        self.registrations_db.append(db_registration)
        self.next_id += 1
        return db_registration

    def get_registration(self, registration_id: int) -> Optional[Registration]:
        for registration in self.registrations_db:
            if registration.id == registration_id:
                return registration
        return None


def get_registrations(self) -> List[Registration]:
    return self.registrations_db


def update_registration(self, registration_id: int, attended: bool) -> Optional[Registration]:
    for i, registration in enumerate(self.registrations_db):
        if registration.id == registration_id:
            registration.attended = attended
            return registration
        return None

    def delete_registration(self, registration_id: int) -> bool:
        initial_len = len(self.registrations_db)
        self.registrations_db = [
            registration for registration in self.registrations_db if registration.id != registration_id]
        return len(self.registrations_db) != initial_len

    def get_registrations_by_event(self, event_id: int) -> List[Registration]:
        return [registration for registration in self.registrations_db if registration.event_id == event_id]

    def get_registrations_by_user(self, user_id: int) -> List[Registration]:
        return [registration for registration in self.registrations_db if registration.user_id == user_id]


registration_service = RegistrationService()
