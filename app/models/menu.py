from app.db.session import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float

class MenuModel(Base):

    __tablename__ = "menu"

    id_menu = Column( Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    description = Column(String)
    inventory = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id_category"))

