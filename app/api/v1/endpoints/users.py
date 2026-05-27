from fastapi import APIRouter, Depends
from app.db import db_user
from app.schemas.user import UserSchema

from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# Create User
@router.post("/")
def create_user( request: UserSchema , db: Session = Depends(get_db)):
    return db_user.create_user( db, request)