from sqlalchemy.orm.session import Session
from app.schemas.reservation import ReservationSchema
from app.models.reservation import ReservationModel

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