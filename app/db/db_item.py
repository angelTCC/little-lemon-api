from sqlalchemy.orm import Session
from app.schemas.reservation import ReservationItemSchema
from app.models.reservation import ReservationItemModel


def create_item(db:Session, request: ReservationItemSchema):

    new_item = ReservationItemModel(
        reservation_id=request.reservation_id,
        menu_id=request.menu_id,
        quantity=request.quantity
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item