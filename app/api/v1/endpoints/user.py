from fastapi import APIRouter, Depends
from app.db import db_user
from app.schemas.user import UserSchema, UserResponseSchema             
from app.models.user import UserModel

from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# CREATE =======================================================
@router.post("/", response_model= UserResponseSchema)
def create( request: UserSchema , db: Session = Depends(get_db)):
    return db_user.create_user( db, request)
"""
# Get User
@router.get("/{user_id}")
def get(user_id:int, db: Session = Depends(get_db)):
    return "get user with id: " + str(user_id)

# Update User
@router.put("/{user_id}")
def update(user_id:int, db: Session = Depends(get_db)):
    return "update user with id: " + str(user_id)

# Delete User
@router.delete("/{user_id}")
def delete(user_id:int, db: Session = Depends(get_db)):
    return "delete user with id: " + str(user_id)"""