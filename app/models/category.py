from sqlalchemy import Column, Integer, String
from app.db.session import Base

class CategoryModel(Base):

    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, index=True)
    name = Column(String)