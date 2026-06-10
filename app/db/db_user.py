from sqlalchemy.orm.session import Session
from app.schemas.user import UserSchema
from app.models.user import UserModel

from app.db.hash import Hash

from fastapi import HTTPException, status

# ORM function to create a new user in the database
def create_user(db: Session, request: UserSchema):
    
    new_user = UserModel(
        name = request.name,
        email = request.email,
        hashed_password = Hash.get_password_hash(request.hashed_password),
    ) 

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# ORM function to get a user from the database
def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id_user == user_id).first()

def get_user_by_username(db: Session, username: str):
  user = db.query(UserModel).filter(UserModel.name == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with username {username} not found')
  return user