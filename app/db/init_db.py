# Import the shared SQLAlchemy engine and Base object
from app.db.session import engine, Base

# Import all models so they are registered inside Base.metadata
from app.models.user import UserModel
from app.models.menu import MenuModel
from app.models.category import CategoryModel
from app.models.menu import MenuModel  
from app.models.reservation import ReservationModel


# Create all registered tables in the database
Base.metadata.create_all(bind=engine)

print("Database initialized successfully!")



