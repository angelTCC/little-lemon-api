from app.db.session import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)