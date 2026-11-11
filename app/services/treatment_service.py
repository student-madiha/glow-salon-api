from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Treatment


def list_treatments(db: Session):
    return db.scalars(select(Treatment)).all()


def find_treatment(db: Session, treatment_id: int):
    return db.get(Treatment, treatment_id)