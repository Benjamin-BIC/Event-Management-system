from pydantic import BaseModel
from datetime import datetime


class RegistrationBase(BaseModel):
    event_id: int
    user_id: int


class RegistrationCreate(RegistrationBase):
    pass


class Registration(RegistrationBase):
    id: int
    registration_date: datetime
    attended: bool = False
