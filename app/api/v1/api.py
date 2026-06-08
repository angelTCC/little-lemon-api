from fastapi import APIRouter
from app.api.v1.endpoints import user
from app.api.v1.endpoints import reservation
from app.api.v1.endpoints import item

api_router = APIRouter()

api_router.include_router( user.router, tags=["users"], prefix="/users" )
api_router.include_router( reservation.router, tags=["reservations"], prefix="/reservations" )
api_router.include_router( item.router, tags=["items"], prefix="/items" )

@api_router.get("/")
def  index():
    return {"message": "Welcome to the Little Lemon API!"}