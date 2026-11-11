from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.booking import BookingCreate, BookingOut
from app.services import booking_service

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("")
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    new_booking = booking_service.create_booking(db, booking)
    return {"message": "Booking confirmed!", "booking": BookingOut.model_validate(new_booking)}


@router.get("", response_model=list[BookingOut])
def list_bookings(db: Session = Depends(get_db)):
    return booking_service.list_bookings(db)


@router.get("/{booking_id}", response_model=BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = booking_service.find_booking(db, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.delete("/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    customer_name = booking_service.cancel_booking(db, booking_id)
    return {"message": f"Booking {booking_id} for {customer_name} has been cancelled"}