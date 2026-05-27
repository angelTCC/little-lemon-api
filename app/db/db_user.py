from sqlalchemy.orm.session import Session
from app.schemas.user import UserSchema
from app.models.user import UserModel

from app.db.hash import Hash

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
