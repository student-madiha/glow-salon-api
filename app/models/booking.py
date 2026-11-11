from datetime import date, time

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.treatment import Treatment


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    treatment_id: Mapped[int] = mapped_column(ForeignKey("treatments.id"))
    appointment_date: Mapped[date]
    appointment_time: Mapped[time]
    notes: Mapped[str | None] = mapped_column(String(255))

    treatment: Mapped[Treatment] = relationship()

    __table_args__ = (
        UniqueConstraint("appointment_date", "appointment_time", name="one_booking_per_slot"),
    )

    @property
    def treatment_name(self):
        return self.treatment.name

    @property
    def price(self):
        return self.treatment.price