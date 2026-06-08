from fastapi import FastAPI

# Import the API router
from app.api.v1.api import api_router

app = FastAPI()

# Include the API router
app.include_router(api_router)
