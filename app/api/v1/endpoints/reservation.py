from fastapi import APIRouter, Depends
from app.db import db_reservation
from app.schemas.reservation import ReservationResponseSchema, ReservationSchema

from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# CREATE =======================================================
@router.post("/", response_model=ReservationResponseSchema)
def create(request: ReservationSchema, db: Session = Depends(get_db)):
    return db_reservation.create_reservation(db, request)


@router.get("/{reservation_id}", response_model=ReservationResponseSchema)
def get(reservation_id: int, db: Session = Depends(get_db)):
    return db_reservation.get_reservation(db, reservation_id)
