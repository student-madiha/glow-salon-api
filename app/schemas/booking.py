from datetime import date, time
from pydantic import BaseModel, ConfigDict


class BookingCreate(BaseModel):
    customer_name: str
    phone: str
    treatment_id: int
    appointment_date: date
    appointment_time: time
    notes: str | None = None


class BookingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_name: str
    phone: str
    treatment_id: int
    appointment_date: date
    appointment_time: time
    notes: str | None = None
    treatment_name: str
    price: int