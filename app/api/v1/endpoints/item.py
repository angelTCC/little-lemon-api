from fastapi import APIRouter, Depends
from app.schemas.reservation import ReservationItemSchema, ReservationItemResponseSchema
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.db import db_item

router = APIRouter()

@router.post("/", response_model=ReservationItemResponseSchema)
def create( request: ReservationItemSchema, db: Session = Depends(get_db)):
    return db_item.create_item(db, request)
