from app.db.session import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class UserModel(Base):

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    
    reservations = relationship("ReservationModel", back_populates="client")