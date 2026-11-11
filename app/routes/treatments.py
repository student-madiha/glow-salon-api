from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.treatment import TreatmentOut
from app.services import treatment_service

router = APIRouter(prefix="/treatments", tags=["Treatments"])


@router.get("", response_model=list[TreatmentOut])
def list_treatments(db: Session = Depends(get_db)):
    return treatment_service.list_treatments(db)


@router.get("/{treatment_id}", response_model=TreatmentOut)
def get_treatment(treatment_id: int, db: Session = Depends(get_db)):
    treatment = treatment_service.find_treatment(db, treatment_id)
    if treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return treatment