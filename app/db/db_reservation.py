from sqlalchemy.orm.session import Session
from app.schemas.reservation import ReservationSchema
from app.models.reservation import ReservationModel

from fastapi import HTTPException, status

def create_reservation(db:Session, request: ReservationSchema):
    
    new_reservation = ReservationModel(
        client_id = request.client_id,
        status = request.status
    )

    # SQLAlchemy ORM no valida automaticamente antes de hacer los querys
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return new_reservation

def get_reservation(db: Session, id: int):
    reservation = db.query(ReservationModel).filter(ReservationModel.id_reservation == id).first()
    return reservation

def delete_reservation(db: Session, reservation_id: int, user_id: int):
    reservation = db.query(ReservationModel).filter(ReservationModel.id_reservation == reservation_id).first()
    if not reservation:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Reservation with id {reservation_id} not found')
    if reservation.client_id != user_id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
            detail='Only reservation creator can delete reservation')

    db.delete(reservation)
    db.commit()
    return 'ok'
