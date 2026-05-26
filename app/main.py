from fastapi import FastAPI

# Import the shared SQLAlchemy engine and Base object
from app.db.session import engine, Base

# Import all models so they are registered inside Base.metadata
from app.db.base import *

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}

# Create all registered tables in the database
Base.metadata.create_all(bind=engine)