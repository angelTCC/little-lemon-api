from fastapi import FastAPI

from app.models import base_all # <- registra todos los modelos en la base.metadata

# Import the API router
from app.api.v1.api import api_router

app = FastAPI()

# Include the API router
app.include_router(api_router)
