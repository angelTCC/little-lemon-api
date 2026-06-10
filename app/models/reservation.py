from sqlalchemy import Column, Enum, Integer, ForeignKey
from app.db.session import Base
from sqlalchemy.orm import relationship

class ReservationModel(Base):

    __tablename__ = "reservations"

    id_reservation = Column(Integer, primary_key=True, index=True)
    client_id = Column( Integer, ForeignKey("users.id_user"), nullable=False)
    status = Column(
        Enum( "pending", "confirmed", "cancelled", name="reservation_status" )
    )

    client = relationship("UserModel", back_populates="reservations")
    items = relationship("ReservationItemModel", back_populates="reservation")

class ReservationItemModel(Base):

    __tablename__ = "reservation_items"

    id_item = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(
        Integer,
        ForeignKey("reservations.id_reservation", ondelete="CASCADE")
        )
    menu_id = Column( Integer, ForeignKey("menu.id_menu"))
    quantity = Column(Integer)

    reservation = relationship("ReservationModel", back_populates="items")