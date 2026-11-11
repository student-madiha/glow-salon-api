from datetime import date

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Booking
from app.schemas.booking import BookingCreate
from app.services.treatment_service import find_treatment


def list_bookings(db: Session):
    return db.scalars(select(Booking)).all()


def create_booking(db: Session, booking: BookingCreate):
    # Rule 1: the treatment must exist
    treatment = find_treatment(db, booking.treatment_id)
    if treatment is None:
        raise HTTPException(status_code=404, detail="That treatment doesn't exist")

    # Rule 2: no dates in the past
    if booking.appointment_date < date.today():
        raise HTTPException(status_code=400, detail="You can't book a date in the past")

    # Rule 3: no double-booking
    existing = db.scalars(
        select(Booking).where(
            Booking.appointment_date == booking.appointment_date,
            Booking.appointment_time == booking.appointment_time,
        )
    ).first()
    if existing is not None:
        raise HTTPException(status_code=409, detail="Sorry, that time slot is already taken")

    # All rules passed, so save the booking
    new_booking = Booking(**booking.model_dump())
    db.add(new_booking)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Sorry, that time slot is already taken")
    db.refresh(new_booking)
    return new_booking


def find_booking(db: Session, booking_id: int):
    return db.get(Booking, booking_id)


def cancel_booking(db: Session, booking_id: int):
    booking = find_booking(db, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    customer_name = booking.customer_name
    db.delete(booking)
    db.commit()
    return customer_name